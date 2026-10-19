#!/usr/bin/env python3
"""LORE auto-factory: the deterministic half of the pipeline.

Agents author, judge and edit; this script does everything that can be checked
or computed exactly: work selection and state, claim banks, technique picks,
blinding, assembly, graph validation, scoring, publishing and status.

Run `python3 scripts/factory.py -h` for the commands. Standard library only.
"""

import argparse
import datetime as dt
import hashlib
import json
import random
import re
import shutil
import sys
from collections import deque
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FACTORY = ROOT / "factory"
STATE = FACTORY / "state"
WORKSHOP = ROOT / "workshop"
MODULES = ROOT / "modules"
NOTES = ROOT / "notes"
EVIDENCE = ROOT / "evidence"

STAGES = ["research", "traps", "analysis", "design", "author", "judge", "edit", "assemble",
          "report", "evaluate", "refine", "publish", "done"]
SEGMENT_TYPES = ["hook", "retrieve", "mechanism", "clinical", "diagnosis",
                 "management", "traps", "consolidate"]
ROLES = {"probe", "explain", "feedback", "hint", "case", "recap", "bridge", "end"}
CHOICE_KINDS = {"correct", "partial", "trap", "help", "continue", "retry",
                "skip", "deeper", "agency"}
# Buttons only: a node may carry nothing that asks the learner to type or that calls a model.
NODE_KEYS = {"role", "say", "choices", "objectives", "ask_confidence", "sure_note", "end", "segment"}
CHOICE_KEYS = {"label", "next", "kind", "trap"}
ERROR_TYPES = {f"E{i}" for i in range(1, 11)}
CLAIM_RE = re.compile(r"^(?:([a-z-]+/[a-z0-9-]+)#)?(K\d+)$")


# ---------------------------------------------------------------- helpers

def today():
    return dt.date.today().isoformat()


def now():
    return dt.datetime.now().isoformat(timespec="seconds")


def read_json(path, default=None):
    path = Path(path)
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def die(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(1)


def split_module(module):
    if module.count("/") != 1:
        die(f"module must be <subject>/<slug>, got {module!r}")
    return module.split("/")


def state_path(module):
    return STATE / (module.replace("/", "--") + ".json")


def work(module):
    return WORKSHOP / module


def _scalar(v):
    v = v.strip()
    if v.startswith("[") and v.endswith("]"):
        inner = v[1:-1].strip()
        return [_scalar(x) for x in inner.split(",")] if inner else []
    if v in ("true", "false"):
        return v == "true"
    if len(v) >= 2 and v[0] == v[-1] and v[0] in "'\"":
        return v[1:-1]
    for cast in (int, float):
        try:
            return cast(v)
        except ValueError:
            pass
    return v


def load_config():
    """Parse the ```yaml Config block in CLAUDE.md (nested maps, scalars, inline lists)."""
    text = (ROOT / "CLAUDE.md").read_text(encoding="utf-8")
    m = re.search(r"```yaml\n(.*?)```", text, re.S)
    if not m:
        die("no ```yaml config block in CLAUDE.md")
    root, stack = {}, [(-1, None)]
    stack[0] = (-1, root)
    for raw in m.group(1).splitlines():
        line = re.sub(r"\s+#.*$", "", raw).rstrip()
        if not line.strip() or line.strip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        key, _, val = line.strip().partition(":")
        while stack[-1][0] >= indent:
            stack.pop()
        parent = stack[-1][1]
        if val.strip():
            parent[key] = _scalar(val)
        else:
            parent[key] = {}
            stack.append((indent, parent[key]))
    return root


CFG = None


def cfg(*keys, default=None):
    global CFG
    if CFG is None:
        CFG = load_config()
    node = CFG
    for k in keys:
        if not isinstance(node, dict) or k not in node:
            return default
        node = node[k]
    return node


# ---------------------------------------------------------------- state & queue

def load_state(module):
    st = read_json(state_path(module))
    if st is None:
        die(f"no state for {module}; run `start` first")
    return st


def save_state(st):
    write_json(state_path(st["module"]), st)


def log(st, stage, result):
    st["history"].append({"at": now(), "stage": stage, "result": result})


def read_queue():
    """Rows of factory/queue.md: | priority | subject | topic | added_by |."""
    path = FACTORY / "queue.md"
    rows = []
    if not path.exists():
        return rows
    for line in path.read_text(encoding="utf-8").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or not cells[0].isdigit():
            continue
        rows.append({"priority": int(cells[0]), "subject": cells[1], "topic": cells[2],
                     "added_by": cells[3] if len(cells) > 3 else ""})
    rows.sort(key=lambda r: r["priority"])
    return rows


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def all_states():
    return [read_json(p) for p in sorted(STATE.glob("*.json"))]


def cmd_start(a):
    module = f"{a.subject}/{slugify(a.slug or a.topic)}"
    if state_path(module).exists() and not a.force:
        die(f"{module} already has state")
    st = {"module": module, "topic": a.topic, "subject": a.subject, "stage": "research",
          "round": 0, "attempts": 0, "blocked": None, "created": now(),
          "published": None, "history": []}
    log(st, "start", "queued topic picked up")
    save_state(st)
    print(module)


DR = ROOT / "design-refinement"


def next_experiment():
    """First EXP-nnn in experiments/plan.md with no row in experiments/registry.md."""
    plan, reg = DR / "experiments" / "plan.md", DR / "experiments" / "registry.md"
    if not plan.exists():
        return None
    done = set(re.findall(r"EXP-\d{3}", reg.read_text(encoding="utf-8"))) if reg.exists() else set()
    for e in dict.fromkeys(re.findall(r"^#+\s*(EXP-\d{3})", plan.read_text(encoding="utf-8"), re.M)):
        if e not in done:
            return e
    return None


def cmd_experiment_done(a):
    states = all_states()
    write_json(FACTORY / "design-state.json", {"published_at_last_experiment": sum(1 for s in states if s["stage"] == "done"),
                                               "last_experiment": a.exp, "at": now()})
    print(f"recorded {a.exp}; next experiment after {cfg('design_refinement', 'every_n_modules', default=2)} more published modules")


def cmd_next(a):
    """Decide what one tick should do. Prints JSON."""
    if (FACTORY / "STOP").exists():
        print(json.dumps({"action": "stop", "why": "factory/STOP exists"}))
        return
    states = all_states()
    active = [s for s in states if s["stage"] != "done" and not s.get("blocked")]
    known = {s["module"] for s in states}
    pending = [r for r in read_queue()
               if f"{r['subject']}/{slugify(r['topic'])}" not in known]
    room = len(active) < cfg("factory", "max_modules_in_progress", default=1)
    if active and not (room and pending):
        active.sort(key=lambda s: -STAGES.index(s["stage"]))
        s = active[0]
        print(json.dumps({"action": "stage", "module": s["module"], "stage": s["stage"],
                          "round": s["round"], "topic": s["topic"]}))
        return
    # Re-research published modules that have gone stale.
    limit = cfg("factory", "refresh_after_days", default=180)
    for s in states:
        if s["stage"] == "done" and s.get("published"):
            age = (dt.date.today() - dt.date.fromisoformat(s["published"][:10])).days
            if age >= limit:
                print(json.dumps({"action": "refresh", "module": s["module"], "topic": s["topic"],
                                  "subject": s["subject"], "age_days": age}))
                return
    exp = next_experiment()
    published = sum(1 for s in states if s["stage"] == "done")
    last = read_json(FACTORY / "design-state.json", {}).get("published_at_last_experiment", 0)
    if exp and published - last >= cfg("design_refinement", "every_n_modules", default=2):
        print(json.dumps({"action": "refine-design", "experiment": exp, "published": published}))
        return
    if len(pending) < cfg("factory", "queue_min", default=3):
        print(json.dumps({"action": "plan", "pending": len(pending)}))
        return
    r = pending[0]
    print(json.dumps({"action": "start", "subject": r["subject"], "topic": r["topic"],
                      "module": f"{r['subject']}/{slugify(r['topic'])}"}))


def cmd_advance(a):
    st = load_state(a.module)
    if a.to not in STAGES:
        die(f"unknown stage {a.to}")
    log(st, st["stage"], a.note or f"→ {a.to}")
    st["stage"], st["attempts"] = a.to, 0
    if a.round is not None:
        st["round"] = a.round
    if a.to == "done":
        st["published"] = now()
    save_state(st)
    print(f"{a.module}: {st['stage']} (round {st['round']})")


def cmd_fail(a):
    st = load_state(a.module)
    st["attempts"] += 1
    log(st, st["stage"], f"FAILED: {a.reason}")
    if st["attempts"] >= cfg("factory", "max_stage_attempts", default=2):
        st["blocked"] = f"{st['stage']}: {a.reason}"
    save_state(st)
    print(f"{a.module}: attempts {st['attempts']}" + (f", BLOCKED ({st['blocked']})" if st["blocked"] else ""))


def cmd_unblock(a):
    st = load_state(a.module)
    st["blocked"], st["attempts"] = None, 0
    log(st, st["stage"], "unblocked")
    save_state(st)
    print(f"{a.module}: unblocked at {st['stage']}")


# ---------------------------------------------------------------- claim bank

MARK_RE = re.compile(r"\[(\d+)\]")


def _norm(text):
    text = MARK_RE.sub("", text).replace("**", "").replace("⚠ Unverified", "")
    return re.sub(r"[^a-z0-9%]+", " ", text.lower()).strip()


def _clean(text):
    text = text.replace("⚠ Unverified", "")
    text = MARK_RE.sub("", text)
    return re.sub(r"\s+([,.;:])", r"\1", re.sub(r"\s{2,}", " ", text)).strip()


def parse_note(path):
    lines = Path(path).read_text(encoding="utf-8").splitlines()
    if lines and lines[0] == "---":
        end = lines.index("---", 1)
        lines = lines[end + 1:]
    claims, refs, section, sub = [], {}, "Summary", None
    for line in lines:
        s = line.strip()
        if s.startswith("## "):
            section, sub = s[3:].strip(), None
            continue
        if s.startswith("# ") or not s:
            continue
        if section == "References":
            m = re.match(r"(\d+)\.\s+(.*)", s)
            if m:
                url = re.search(r"https?://\S+", m.group(2))
                tier = re.search(r"tier (\d|K)", m.group(2))
                refs[m.group(1)] = {
                    "title": re.split(r"\s+https?://", m.group(2))[0].rstrip(". "),
                    "url": url.group(0) if url else "",
                    "tier": (int(tier.group(1)) if tier.group(1).isdigit() else tier.group(1)) if tier else None}
            continue
        if section.startswith("Unverified"):
            continue
        if re.fullmatch(r"\*\*[^*]+\*\*", s):
            sub = s.strip("*")
            continue
        if s.startswith("|"):
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 3 and MARK_RE.search(cells[-1]):
                text = f"{_clean(cells[0])} — {_clean(cells[1])}"
                claims.append({"text": text, "refs": MARK_RE.findall(cells[-1]),
                               "unverified": "⚠" in s, "section": section, "sub": sub,
                               "kind": "table"})
            continue
        body = re.sub(r"^(>|-|\*|\d+\.)\s*", "", s)
        if MARK_RE.search(body):
            kind = "exam-note" if "Exam notes" in section else "fact"
            claims.append({"text": _clean(body), "refs": list(dict.fromkeys(MARK_RE.findall(body))),
                           "unverified": "⚠ Unverified" in body, "section": section,
                           "sub": sub, "kind": kind})
    return claims, refs


def cmd_bank(a):
    subject, slug = split_module(a.module)
    note = NOTES / subject / f"{slug}.md"
    if not note.exists():
        die(f"no note at {note}")
    parsed, refs = parse_note(note)
    ledger = {}
    lpath = EVIDENCE / subject / slug / "ledger.md"
    if lpath.exists():
        for row in lpath.read_text(encoding="utf-8").splitlines():
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) >= 4 and re.fullmatch(r"C\d+", cells[0]):
                ledger[_norm(cells[1])] = cells[0]
    claims = {}
    for i, c in enumerate(parsed, 1):
        entry = {"text": c["text"], "refs": c["refs"],
                 "status": "unverified" if c["unverified"] else "verified",
                 "section": c["section"] + (f" / {c['sub']}" if c["sub"] else ""),
                 "hy": c["section"] in ("High-yield", "Summary") or c["section"].startswith("Most common"),
                 "kind": c["kind"]}
        if _norm(c["text"]) in ledger:
            entry["ledger"] = ledger[_norm(c["text"])]
        missing = [r for r in c["refs"] if r not in refs]
        if missing:
            entry["missing_refs"] = missing
        claims[f"K{i}"] = entry
    prov = re.search(r"^provenance:\s*(\S+)", note.read_text(encoding="utf-8"), re.M)
    bank = {"module": a.module, "note": str(note.relative_to(ROOT)), "built": today(),
            "provenance": prov.group(1) if prov else "sources",
            "references": refs, "claims": claims}
    write_json(work(a.module) / "claim-bank.json", bank)
    ver = sum(c["status"] == "verified" for c in claims.values())
    print(f"claim bank: {len(claims)} claims ({ver} verified, {len(claims) - ver} unverified), "
          f"{sum(c['hy'] for c in claims.values())} high-yield, {len(refs)} references")


# ---------------------------------------------------------------- techniques & tournament

def read_techniques():
    text = (ROOT / "reference" / "techniques.md").read_text(encoding="utf-8")
    techs = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 3 and re.fullmatch(r"T\d+", cells[0]):
            techs[cells[0]] = {"name": cells[1], "fits": [f.strip() for f in cells[2].split(",")]}
    return techs


def stats_path():
    return FACTORY / "technique-stats.json"


def cmd_pick(a):
    """Choose competing techniques for one segment: exploit the best, explore the least tried."""
    techs = read_techniques()
    k = a.k or cfg("tournament", "variants_per_segment", default=3)
    explore = min(cfg("tournament", "explore_picks", default=1), k)
    min_trials = cfg("tournament", "min_trials_before_exploit", default=3)
    stats = read_json(stats_path(), {"by_type": {}}).get("by_type", {}).get(a.type, {})
    pool = [t for t, v in techs.items() if a.type in v["fits"]] or list(techs)
    rng = random.Random(f"{a.seed}:{a.type}")
    picks = [t for t in (a.require or []) if t in techs][:k]

    def rec(t):
        return stats.get(t, {"trials": 0, "wins": 0, "score_sum": 0})

    tried = [t for t in pool if rec(t)["trials"] >= min_trials and t not in picks]
    tried.sort(key=lambda t: (-(rec(t)["wins"] / rec(t)["trials"]),
                              -(rec(t)["score_sum"] / rec(t)["trials"])))
    for t in tried:
        if len(picks) >= k - explore:
            break
        picks.append(t)
    rest = [t for t in pool if t not in picks]
    rng.shuffle(rest)
    rest.sort(key=lambda t: rec(t)["trials"])
    for t in rest:
        if len(picks) >= k:
            break
        picks.append(t)
    print(json.dumps({"type": a.type, "techniques": [{"id": t, "name": techs[t]["name"],
                     "trials": rec(t)["trials"]} for t in picks]}))


def cmd_blind(a):
    src = work(a.module) / "variants" / a.segment
    files = sorted(src.glob("*.json"))
    if not files:
        die(f"no variants in {src}")
    dst = work(a.module) / "blind" / a.segment
    if dst.exists():
        shutil.rmtree(dst)
    bp, bank = read_json(work(a.module) / "blueprint.json"), load_bank(a.module)
    dropped = []
    for f in list(files):
        if validate_segment(a.module, read_json(f), bp, bank)["errors"]:
            files.remove(f)
            dropped.append(f.stem)
    if not files:
        die(f"{a.segment}: no variant passes check-segment (dropped {', '.join(dropped)})")
    rng = random.Random(f"{a.module}:{a.segment}:{len(files)}")
    rng.shuffle(files)
    mapping = {}
    for label, f in zip("abcdefgh", files):
        data = read_json(f)
        mapping[label] = data.get("technique", f.stem)
        data.pop("technique", None)
        data.pop("notes", None)
        write_json(dst / f"{label}.json", data)
    write_json(dst / "map.json", mapping)
    print(f"{a.segment}: {len(files)} variants blinded as {', '.join(mapping)}"
          + (f"; dropped (check-segment errors): {', '.join(dropped)}" if dropped else ""))


def cmd_record(a):
    """After the editor decides a segment: update technique stats and the playbook."""
    w = work(a.module)
    sel = read_json(w / "selection" / f"{a.segment}.json")
    mapping = read_json(w / "blind" / a.segment / "map.json")
    bp = read_json(w / "blueprint.json")
    if not (sel and mapping and bp):
        die("need selection, blind map and blueprint")
    seg = next(s for s in bp["segments"] if s["id"] == a.segment)
    scores = {}
    for jf in (w / "judging").glob(f"{a.segment}-*.json"):
        for label, v in read_json(jf)["variants"].items():
            scores.setdefault(label, []).append(float(v.get("weighted") or 0))
    stats = read_json(stats_path(), {"by_type": {}})
    bucket = stats["by_type"].setdefault(seg["type"], {})
    used = sel.get("used", [])
    for label, tech in mapping.items():
        r = bucket.setdefault(tech, {"trials": 0, "wins": 0, "score_sum": 0})
        r["trials"] += 1
        r["score_sum"] = round(r["score_sum"] + (sum(scores.get(label, [0])) / max(1, len(scores.get(label, [])))), 3)
        if label == sel["primary"]:
            r["wins"] += 1
        elif label in used:
            r["wins"] += 0.5
    stats["updated"] = now()
    write_json(stats_path(), stats)
    final = read_json(w / "segments" / f"{a.segment}.json")
    if final is not None:
        final["technique"] = "+".join(mapping[l] for l in [sel["primary"]] + [u for u in used if u != sel["primary"]])
        final["decision"] = sel["decision"]
        write_json(w / "segments" / f"{a.segment}.json", final)
    lesson = sel.get("lesson", "").strip()
    if lesson:
        losers = [mapping[l] for l in mapping if l != sel["primary"]]
        line = (f"- [{seg['type']}] {mapping[sel['primary']]} over {', '.join(losers)} "
                f"({a.module} {a.segment}, {sel['decision']}): {lesson}\n")
        with open(FACTORY / "playbook.md", "a", encoding="utf-8") as fh:
            fh.write(line)
    print(f"{a.segment}: {sel['decision']} primary={mapping[sel['primary']]} used={[mapping[u] for u in used]}")


# ---------------------------------------------------------------- graph checks

def load_bank(module):
    bank = read_json(work(module) / "claim-bank.json")
    if bank is None:
        die(f"no claim bank for {module}; run `bank`")
    return bank


def resolve_claim(cid, module, bank, cache):
    m = CLAIM_RE.match(cid)
    if not m:
        return None
    other, k = m.groups()
    if not other or other == module:
        return bank["claims"].get(k)
    if other not in cache:
        pub = read_json(MODULES / f"{other}.json")
        cache[other] = pub["claims"] if pub else {}
    return cache[other].get(k)


def words(text):
    return len(re.findall(r"\S+", text))


def check_nodes(nodes, module, bank, bp, issues, seg_type_of, prefix=""):
    """Per-node checks shared by segment and module validation."""
    lim_words = cfg("module", "max_words_per_message", default=60)
    lim_msgs = cfg("module", "max_messages_per_node", default=3)
    trap_ids = {t["id"] for t in bp.get("traps", [])}
    obj_ids = {o["id"] for o in bp.get("objectives", [])}
    cache = {}
    for nid, n in nodes.items():
        where = f"{prefix}{nid}"
        role = n.get("role")
        for k in set(n) - NODE_KEYS:
            issues["errors"].append(f"{where}: unknown field {k!r} (buttons only; see reference/module-format.md)")
        if role not in ROLES:
            issues["errors"].append(f"{where}: role {role!r} not one of {sorted(ROLES)}")
        msgs = n.get("say") or []
        if not msgs:
            issues["errors"].append(f"{where}: no messages")
        if len(msgs) > lim_msgs:
            issues["errors"].append(f"{where}: {len(msgs)} messages (max {lim_msgs})")
        extra = [n["sure_note"]] if isinstance(n.get("sure_note"), dict) else []
        for i, msg in enumerate(msgs + extra):
            if not isinstance(msg, dict) or "text" not in msg or "claims" not in msg:
                issues["errors"].append(f"{where}.say[{i}]: needs text and claims")
                continue
            if words(msg["text"]) > lim_words:
                issues["errors"].append(f"{where}.say[{i}]: {words(msg['text'])} words (max {lim_words})")
            unver = False
            for cid in msg["claims"]:
                c = resolve_claim(cid, module, bank, cache)
                if c is None:
                    issues["errors"].append(f"{where}.say[{i}]: unknown claim {cid}")
                elif c.get("status") == "unverified":
                    unver = True
            if unver and msg.get("flag") != "unverified":
                issues["errors"].append(f"{where}.say[{i}]: cites an unverified claim without flag: \"unverified\"")
            if unver:
                issues.setdefault("_unverified_nodes", set()).add(nid)
        for o in n.get("objectives", []):
            if obj_ids and o not in obj_ids:
                issues["errors"].append(f"{where}: unknown objective {o}")
        if n.get("end"):
            if n.get("choices"):
                issues["errors"].append(f"{where}: end node has choices")
            continue
        ch = n.get("choices") or []
        if not 1 <= len(ch) <= 4:
            issues["errors"].append(f"{where}: {len(ch)} choices (need 1–4)")
        kinds = [c.get("kind") for c in ch]
        labels = [c.get("label", "").strip().lower() for c in ch]
        if len(set(labels)) != len(labels):
            issues["errors"].append(f"{where}: two choices share a label")
        for j, c in enumerate(ch):
            for k in set(c) - CHOICE_KEYS:
                issues["errors"].append(f"{where}.choices[{j}]: unknown field {k!r}")
            if c.get("kind") not in CHOICE_KINDS:
                issues["errors"].append(f"{where}.choices[{j}]: kind {c.get('kind')!r} invalid")
            if c.get("kind") == "trap" and c.get("trap") not in trap_ids:
                issues["errors"].append(f"{where}.choices[{j}]: trap {c.get('trap')!r} not in blueprint")
            if c.get("kind") == "trap" and role != "probe":
                issues["errors"].append(f"{where}.choices[{j}]: trap choices belong on probe nodes")
            if words(c.get("label", "")) > 12:
                issues["warnings"].append(f"{where}.choices[{j}]: label over 12 words")
            if not c.get("next"):
                issues["errors"].append(f"{where}.choices[{j}]: no next")
        if role == "probe":
            if "correct" not in kinds:
                issues["errors"].append(f"{where}: probe without a correct choice")
            if "trap" not in kinds:
                issues["errors"].append(f"{where}: probe without a trap choice (every probe must diagnose at least one trap)")
        if role == "probe" and not n.get("objectives"):
            issues["warnings"].append(f"{where}: probe tags no objective")


def edges(nodes, resolve):
    g = {}
    for nid, n in nodes.items():
        g[nid] = []
        for c in n.get("choices") or []:
            t = resolve(c.get("next", ""))
            if t is not None:
                g[nid].append((t, c.get("kind")))
    return g


def reach(g, start, avoid=frozenset(), skip_kinds=frozenset()):
    seen, q = {start}, deque([start])
    if start in avoid:
        return set()
    while q:
        u = q.popleft()
        for v, kind in g.get(u, []):
            if kind in skip_kinds or v in avoid or v in seen:
                continue
            seen.add(v)
            q.append(v)
    return seen


def can_reach(g, targets):
    rev = {}
    for u, outs in g.items():
        for v, _ in outs:
            rev.setdefault(v, set()).add(u)
    seen, q = set(targets), deque(targets)
    while q:
        u = q.popleft()
        for p in rev.get(u, ()):
            if p not in seen:
                seen.add(p)
                q.append(p)
    return seen


def tell_run(nodes, g):
    """Longest chain of consecutive non-interactive nodes (fewer than 2 choices)."""
    passive = {n for n, d in nodes.items() if len(d.get("choices") or []) < 2 and not d.get("end")}
    memo, onstack = {}, set()

    def run(u):
        if u in memo:
            return memo[u]
        if u in onstack:
            raise ValueError(u)
        onstack.add(u)
        best = 0
        for v, _ in g.get(u, []):
            if v in passive:
                best = max(best, run(v))
        onstack.discard(u)
        memo[u] = 1 + best
        return memo[u]

    try:
        return max((run(u) for u in passive), default=0), None
    except ValueError as e:
        return None, str(e)


def path_lengths(g, start, end_nodes):
    dist, q = {start: 0}, deque([start])
    while q:
        u = q.popleft()
        for v, _ in g.get(u, []):
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    shortest = min((dist[e] for e in end_nodes if e in dist), default=None)
    dag = {u: [v for v, k in outs if k != "retry"] for u, outs in g.items()}
    memo = {}

    def longest(u, depth=0):
        if depth > 500:
            raise RecursionError
        if u in memo:
            return memo[u]
        memo[u] = None
        best = 0 if u in end_nodes else -10**9
        for v in dag.get(u, []):
            r = longest(v, depth + 1)
            if r is None:
                raise RecursionError
            best = max(best, r + 1)
        memo[u] = best
        return best

    try:
        lp = longest(start)
        return shortest, (lp if lp >= 0 else None)
    except RecursionError:
        return shortest, None


def validate_segment(module, seg, bp, bank):
    issues = {"errors": [], "warnings": []}
    meta = next((s for s in bp["segments"] if s["id"] == seg.get("segment")), None)
    if meta is None:
        issues["errors"].append(f"segment {seg.get('segment')!r} not in blueprint")
        return issues
    nodes = seg.get("nodes") or {}
    if seg.get("entry") not in nodes:
        issues["errors"].append(f"entry {seg.get('entry')!r} is not a node")
        return issues
    routes = set(meta.get("routes", []))
    check_nodes(nodes, module, bank, bp, issues, None, prefix=f"{meta['id']}.")
    exits = set()

    def resolve(t):
        if t.startswith("@"):
            if t in ("@next", "@end") or t[1:] in routes:
                exits.add(t)
                return "@EXIT"
            issues["errors"].append(f"{meta['id']}: route {t} not allowed (blueprint routes: {sorted(routes) or 'none'})")
            return None
        if t not in nodes:
            issues["errors"].append(f"{meta['id']}: next {t!r} is not a node")
            return None
        return t

    g = edges(nodes, resolve)
    g["@EXIT"] = []
    seen = reach(g, seg["entry"])
    for n in nodes:
        if n not in seen:
            issues["errors"].append(f"{meta['id']}.{n}: unreachable from entry")
    ok = can_reach(g, ["@EXIT"] + [n for n, d in nodes.items() if d.get("end")])
    for n in nodes:
        if n not in ok:
            issues["errors"].append(f"{meta['id']}.{n}: cannot reach the segment exit")
    if "@EXIT" not in seen and not any(nodes[n].get("end") for n in seen):
        issues["errors"].append(f"{meta['id']}: no exit")
    tr, loop = tell_run(nodes, g)
    lim = cfg("module", "max_tell_run", default=2)
    if loop:
        issues["errors"].append(f"{meta['id']}.{loop}: loop of non-interactive nodes")
    elif tr > lim:
        issues["errors"].append(f"{meta['id']}: {tr} non-interactive nodes in a row (max {lim})")
    for o in meta.get("objectives", []):
        if not any(o in d.get("objectives", []) for d in nodes.values()):
            issues["errors"].append(f"{meta['id']}: objective {o} assigned to this segment but no node tags it")
    for t in meta.get("traps", []):
        if not any(c.get("trap") == t for d in nodes.values() for c in d.get("choices") or []):
            issues["errors"].append(f"{meta['id']}: trap {t} assigned to this segment but no choice offers it")
    if meta["type"] == "consolidate" and not seg.get("cards"):
        issues["warnings"].append(f"{meta['id']}: consolidate segment with no cards")
    for i, card in enumerate(seg.get("cards", [])):
        for cid in card.get("claims", []):
            if resolve_claim(cid, module, bank, {}) is None:
                issues["errors"].append(f"{meta['id']}.cards[{i}]: unknown claim {cid}")
        if not card.get("claims"):
            issues["errors"].append(f"{meta['id']}.cards[{i}]: card answer cites no claim")
    issues.pop("_unverified_nodes", None)
    return issues


def cmd_check_segment(a):
    bp = read_json(work(a.module) / "blueprint.json")
    if bp is None:
        die("no blueprint.json")
    issues = validate_segment(a.module, read_json(a.path), bp, load_bank(a.module))
    print(json.dumps(issues, indent=2))
    sys.exit(1 if issues["errors"] else 0)


# ---------------------------------------------------------------- assemble

def cmd_assemble(a):
    w = work(a.module)
    bp, bank = read_json(w / "blueprint.json"), load_bank(a.module)
    segs = bp["segments"]
    nodes, cards, seg_meta = {}, [], []
    loaded = {}
    for s in segs:
        data = read_json(w / "segments" / f"{s['id']}.json")
        if data is None:
            die(f"missing segments/{s['id']}.json")
        loaded[s["id"]] = data
    need_end = False
    for i, s in enumerate(segs):
        data = loaded[s["id"]]
        nxt = f"{segs[i + 1]['id']}.{loaded[segs[i + 1]['id']]['entry']}" if i + 1 < len(segs) else "END"
        for nid, n in data["nodes"].items():
            n = json.loads(json.dumps(n))
            for c in n.get("choices") or []:
                t = c.get("next", "")
                if t == "@next":
                    c["next"] = nxt
                elif t == "@end":
                    c["next"] = "END"
                elif t.startswith("@S"):
                    c["next"] = f"{t[1:]}.{loaded[t[1:]]['entry']}" if t[1:] in loaded else t
                else:
                    c["next"] = f"{s['id']}.{t}"
                need_end |= c["next"] == "END"
            n["segment"] = s["id"]
            nodes[f"{s['id']}.{nid}"] = n
        for card in data.get("cards", []):
            cards.append(dict(card, segment=s["id"],
                              schedule_days=cfg("module", "card_schedule_days", default=[1, 3, 7, 21, 60])))
        seg_meta.append({"id": s["id"], "title": s.get("title", ""), "type": s["type"],
                         "entry": f"{s['id']}.{data['entry']}", "technique": data.get("technique", ""),
                         "decision": data.get("decision", "")})
    if need_end:
        nodes["END"] = {"role": "end", "end": True, "segment": segs[-1]["id"],
                        "say": [{"text": bp.get("closing", "That's the module. Your review cards are below: "
                                 "come back to them on the days shown."), "claims": []}]}
    used = set()
    for n in nodes.values():
        for msg in (n.get("say") or []) + ([n["sure_note"]] if isinstance(n.get("sure_note"), dict) else []):
            used.update(msg.get("claims", []))
    for card in cards:
        used.update(card.get("claims", []))
    report = read_json(w / "report.json")
    for msg in iter_report(report):
        used.update(msg.get("claims", []))
    claims, cache = {}, {}
    for cid in sorted(used, key=lambda c: (("#" in c), int(re.sub(r"\D", "", c.split("#")[-1]) or 0), c)):
        c = resolve_claim(cid, a.module, bank, cache)
        if c:
            claims[cid] = {k: c[k] for k in ("text", "refs", "status") if k in c}
    refs = {}
    for cid, c in claims.items():
        if "#" in cid:
            continue
        for r in c["refs"]:
            if r in bank["references"]:
                refs[r] = bank["references"][r]
    prev = read_json(MODULES / f"{a.module}.json")
    module = {"schema": "lore.module/v1", "id": a.module, "title": bp.get("title", a.module),
              "subject": a.module.split("/")[0], "exam": "NEET PG / INI-CET",
              "version": (prev["version"] + 1) if prev else 1, "built": today(), "status": "draft",
              "provenance": bank.get("provenance", "sources"),
              "summary": bp.get("summary", ""),
              "objectives": bp.get("objectives", []), "traps": bp.get("traps", []),
              "segments": seg_meta, "start": seg_meta[0]["entry"], "nodes": nodes,
              "claims": claims, "references": dict(sorted(refs.items(), key=lambda kv: int(kv[0]))),
              "cards": cards}
    if report:
        module["report"] = report
    write_json(w / "module.json", module)
    print(f"assembled {len(nodes)} nodes, {len(segs)} segments, {len(claims)} claims, {len(cards)} cards")


# ---------------------------------------------------------------- report (pre-authored, path-driven)

REPORT_SHAPE = {
    "headline": ["strong", "mixed", "weak"],
    "calibration": ["overconfident", "underconfident", "calibrated"],
    "help": ["hints_heavy", "hints_none", "hinted_only"],
    "next_steps": ["gap", "clear"],
}
TRAP_STATUSES = ["avoided", "fell_recovered", "fell_open"]
LEVELS = ["secure", "shaky", "gap"]


def iter_report(report):
    if not report:
        return
    stack = [report]
    while stack:
        x = stack.pop()
        if isinstance(x, dict):
            if "text" in x and "claims" in x:
                yield x
            else:
                stack.extend(x.values())


def check_report(mod, issues, require=False):
    rep = mod.get("report")
    if not rep:
        (issues["errors"] if require else issues["warnings"]).append("no report block yet (stage report)")
        return
    def need(path, entry):
        if not isinstance(entry, dict) or "text" not in entry or "claims" not in entry:
            issues["errors"].append(f"report.{path}: missing or not {{text, claims}}")
        elif words(entry["text"]) > 90:
            issues["errors"].append(f"report.{path}: {words(entry['text'])} words (max 90)")
    for sec, keys in REPORT_SHAPE.items():
        for k in keys:
            need(f"{sec}.{k}", (rep.get(sec) or {}).get(k))
    for o in mod.get("objectives", []):
        for lv in LEVELS:
            need(f"objectives.{o['id']}.{lv}", (rep.get("objectives") or {}).get(o["id"], {}).get(lv))
    for t in mod.get("traps", []):
        for st in TRAP_STATUSES:
            need(f"traps.{t['id']}.{st}", (rep.get("traps") or {}).get(t["id"], {}).get(st))
    for et in sorted({t.get("error_type") for t in mod.get("traps", [])} - {None}):
        need(f"error_types.{et}", (rep.get("error_types") or {}).get(et))
    if any(c.get("kind") == "skip" for d in mod["nodes"].values() for c in d.get("choices") or []):
        need("pace.fast_lane", (rep.get("pace") or {}).get("fast_lane"))


def render_report(mod, path):
    """Deterministic report from a path: [{node, choice, sure}]. Mirrors player/index.html."""
    nodes, traps = mod["nodes"], {t["id"]: t for t in mod.get("traps", [])}
    steps = []
    for st in path:
        n = nodes[st["node"]]
        c = n["choices"][st["choice"]]
        steps.append({"node": st["node"], "role": n.get("role"), "kind": c.get("kind"), "trap": c.get("trap"),
                      "sure": st.get("sure"), "objectives": n.get("objectives", []),
                      "offers": [x.get("trap") for x in n["choices"] if x.get("kind") == "trap"]})
    first, seen, helped = [], set(), set()
    for s_ in steps:
        if s_["kind"] == "help":
            helped.add(s_["node"])
        if s_["role"] == "probe" and s_["kind"] in ("correct", "partial", "trap") and s_["node"] not in seen:
            seen.add(s_["node"])
            s_["hinted"] = s_["node"] in helped
            s_["cold"] = not any(c.get("kind") == "help" for c in nodes[s_["node"]]["choices"])
            first.append(s_)
    trap_status = {}
    for tid in traps:
        enc = [s_ for s_ in first if tid in s_["offers"]]
        if not enc:
            trap_status[tid] = "not_met"
            continue
        fell = [i for i, s_ in enumerate(enc) if s_["trap"] == tid]
        if not fell:
            trap_status[tid] = "avoided"
        elif any(s_["kind"] == "correct" for s_ in enc[fell[-1] + 1:]) and enc[-1]["kind"] == "correct":
            trap_status[tid] = "fell_recovered"
        else:
            trap_status[tid] = "fell_open"
    levels = {}
    for o in mod.get("objectives", []):
        ans = [s_ for s_ in first if o["id"] in s_["objectives"]]
        lane = any(s_["kind"] == "skip" and o["id"] in s_["objectives"] for s_ in steps)
        open_trap = any(trap_status.get(t) == "fell_open" for t, d in traps.items() if o["id"] in d.get("objectives", []))
        if not ans and not lane:
            levels[o["id"]] = "unseen"
            continue
        wrong = sum(s_["kind"] != "correct" for s_ in ans)
        sure_wrong = sum(s_["sure"] is True and s_["kind"] != "correct" for s_ in ans)
        guessed = sum(s_["sure"] is False for s_ in ans)
        if open_trap or (ans and wrong * 2 >= len(ans)):
            levels[o["id"]] = "gap"
        elif (wrong == 0 and sure_wrong == 0 and guessed * 2 < max(1, len(ans))) or (lane and wrong == 0):
            levels[o["id"]] = "secure"
        else:
            levels[o["id"]] = "shaky"
    fallen = [t for t, v in trap_status.items() if v.startswith("fell")]
    by_type = {}
    for t in fallen:
        by_type.setdefault(traps[t].get("error_type"), []).append(t)
    conf = [s_ for s_ in first if s_["sure"] is not None]
    sure_wrong = sum(s_["sure"] and s_["kind"] != "correct" for s_ in conf)
    guess_right = sum((s_["sure"] is False) and s_["kind"] == "correct" for s_ in conf)
    calibration = None
    if len(conf) >= 3:
        calibration = "overconfident" if sure_wrong >= 2 else ("underconfident" if guess_right >= 3 and sure_wrong == 0 else "calibrated")
    hints = sum(s_["kind"] == "help" for s_ in steps)
    # DP11: objectives answered right only with a hint, and not right on any cold probe
    hinted_only = sorted({o for s_ in first if s_["hinted"] and s_["kind"] == "correct" for o in s_["objectives"]}
                         - {o for s_ in first if s_["cold"] and s_["kind"] == "correct" for o in s_["objectives"]}
                         - {o for s_ in first if not s_["hinted"] and s_["kind"] == "correct" for o in s_["objectives"]})
    cold = [s_ for s_ in first if s_["cold"]]
    help_ = ("hints_heavy" if hints >= 3 else ("hinted_only" if hinted_only else
             ("hints_none" if hints == 0 and fallen else None)))
    # DP7: traps fallen into while Sure come first, and so do their objectives' cards
    confident = [t for t in traps if any(s_["trap"] == t and s_["sure"] is True for s_ in first)]
    core = [o["id"] for o in mod.get("objectives", []) if o.get("core")]
    gaps = [o for o in core if levels.get(o) == "gap"]
    shaky = [o for o in levels if levels[o] == "shaky"]
    headline = "strong" if not gaps and len(shaky) <= 1 else ("weak" if len(gaps) * 3 >= max(1, len(core)) else "mixed")
    rank = {"gap": 1, "shaky": 2}
    conf_obj = {o for t in confident for o in traps[t].get("objectives", [])}
    cards = sorted(range(len(mod.get("cards", []))),
                   key=lambda i: 0 if mod["cards"][i].get("objective") in conf_obj
                   else rank.get(levels.get(mod["cards"][i].get("objective")), 3))
    rep = mod.get("report") or {}
    def txt(*keys):
        x = rep
        for k in keys:
            x = (x or {}).get(k)
        return (x or {}).get("text")
    texts = [txt("headline", headline)]
    texts += [txt("objectives", o, lv) for o, lv in levels.items() if lv in LEVELS]
    order = confident + [t for t in trap_status if t not in confident]
    texts += [txt("traps", t, trap_status[t]) for t in order if trap_status[t] in TRAP_STATUSES and trap_status[t] != "avoided"]
    texts += [txt("error_types", et) for et, ts in by_type.items() if len(ts) >= 2]
    texts += [txt("calibration", calibration)] if calibration else []
    texts += [txt("help", help_)] if help_ else []
    texts += [txt("pace", "fast_lane")] if any(s_["kind"] == "skip" for s_ in steps) else []
    texts += [txt("next_steps", "gap" if gaps or shaky else "clear")]
    return {"headline": headline, "objectives": levels, "traps": trap_status,
            "error_profile": {k: v for k, v in by_type.items()}, "calibration": calibration,
            "sure_wrong": sure_wrong, "guess_right": guess_right, "hints": hints,
            "fast_lane": any(s_["kind"] == "skip" for s_ in steps),
            "confident_errors": confident, "hinted_only": hinted_only,
            "cold_right": sum(s_["kind"] == "correct" for s_ in cold), "cold_total": len(cold),
            "card_order": cards, "texts": [t for t in texts if t]}


def cmd_render_report(a):
    mod = read_json(Path(a.path_module) if a.path_module else work(a.module) / "module.json")
    path = read_json(a.path)
    path = path.get("path", path) if isinstance(path, dict) else path
    print(json.dumps(render_report(mod, path), indent=2, ensure_ascii=False))



# ---------------------------------------------------------------- lints adopted from design-refinement/principles.md

ABSOLUTES = {"always", "never", "all", "none", "only", "every", "must", "completely", "invariably"}
BANNED = {  # DP14: warning-level unless marked error
    "praise": ["you're so smart", "you are so smart", "genius", "you're a natural", "brilliant!", "perfect!", "amazing!"],
    "control": ["you should have known", "obviously", "as everyone knows", "simply", "just remember"],
    "scold": ["wrong!", "incorrect!", "no!", "careless", "silly mistake", "lazy"],
    "pseudo": ["learning style", "left-brain", "right-brain", "visual learner", "auditory learner"],
}
BANNED_ERRORS = {"scold", "pseudo"}


def _first_words(t, n=3):
    return " ".join(re.findall(r"[a-z0-9]+", t.lower())[:n])


def lint_module(mod, issues, metrics):
    nodes = mod["nodes"]
    probes = {n: d for n, d in nodes.items() if d.get("role") == "probe"}
    key_longest, key_pos, traps_per_probe = 0, {}, []
    for nid, d in probes.items():
        ch = d.get("choices") or []
        answer = [c for c in ch if c.get("kind") in ("correct", "partial", "trap")]
        labels = [c.get("label", "") for c in answer]
        for c in answer:
            if re.search(r"\b(all|none) of the above\b", c.get("label", ""), re.I):
                issues["errors"].append(f"{nid}: 'all/none of the above' option (DP1)")
        key = [c for c in answer if c.get("kind") == "correct"]
        if key and len(answer) > 1:
            k = key[0]["label"]
            lens = [words(l) for l in labels]
            if words(k) == max(lens) and lens.count(max(lens)) == 1:
                key_longest += 1
                issues["warnings"].append(f"{nid}: the correct option is the only longest one (DP1)")
            kw = set(re.findall(r"[a-z]+", k.lower()))
            others = [set(re.findall(r"[a-z]+", l.lower())) for l in labels if l != k]
            if kw & ABSOLUTES and not any(o & ABSOLUTES for o in others):
                issues["warnings"].append(f"{nid}: only the correct option uses an absolute word (DP1)")
            if re.search(r"\d", k) and not any(re.search(r"\d", l) for l in labels if l != k):
                issues["warnings"].append(f"{nid}: only the correct option contains a number (DP1)")
            idx = ch.index(key[0])
            key_pos[idx] = key_pos.get(idx, 0) + 1
        tr = [c.get("trap") for c in ch if c.get("kind") == "trap"]
        traps_per_probe.append(len(tr))
        if len(tr) != len(set(tr)):
            issues["warnings"].append(f"{nid}: two options carry the same trap (DP3)")
        nexts = {}
        for c in ch:
            if c.get("kind") == "trap":
                nexts.setdefault(c.get("next"), set()).add(c.get("trap"))
        if any(len(v) > 1 for v in nexts.values()):
            issues["warnings"].append(f"{nid}: different traps share one feedback node (DP3)")
        fw = [_first_words(l) for l in labels if words(l) >= 3]
        if len(fw) != len(set(fw)):
            issues["warnings"].append(f"{nid}: two options start with the same three words (DP3)")
        q = [m for m in d.get("say", []) if m.get("text", "").rstrip().endswith("?")]
        if len(q) > 1:
            issues["errors"].append(f"{nid}: more than one question in a node (DP26)")
        if d.get("say") and not d["say"][-1].get("text", "").rstrip().endswith("?"):
            issues["warnings"].append(f"{nid}: probe does not end on its question (DP26)")
    # DP5: a trap's probes must differ in surface
    by_trap = {}
    for nid, d in probes.items():
        for c in d.get("choices") or []:
            if c.get("kind") == "trap":
                by_trap.setdefault(c.get("trap"), []).append(nid)
    distinct = 0
    for t, ns in by_trap.items():
        firsts = {(probes[n].get("say") or [{}])[0].get("text", "").strip().lower() for n in ns}
        sets = {frozenset(c.get("label", "").strip().lower() for c in probes[n]["choices"]) for n in ns}
        if len(ns) > 1 and (len(firsts) < len(ns) or len(sets) < len(ns)):
            issues["warnings"].append(f"trap {t}: two of its probes share a stem or an option set; a re-test should vary the surface (DP5)")
        else:
            distinct += 1
    # DP9 hints never leak; DP13 correct feedback says why
    parents = {}
    for nid, d in nodes.items():
        for c in d.get("choices") or []:
            parents.setdefault(c.get("next"), []).append((nid, c))
    for nid, d in nodes.items():
        text = " ".join(m.get("text", "") for m in d.get("say") or []).lower()
        if d.get("role") == "hint":
            for pid, c in parents.get(nid, []):
                for k in (nodes[pid].get("choices") or []):
                    if k.get("kind") == "correct" and len(k.get("label", "")) > 3 and k["label"].lower() in text:
                        issues["warnings"].append(f"{nid}: hint contains the answer '{k['label']}' (DP9)")
        if any(c.get("kind") == "correct" for _, c in parents.get(nid, [])) and d.get("role") == "feedback":
            if words(text) < 8 or not any(m.get("claims") for m in d.get("say") or []):
                issues["warnings"].append(f"{nid}: feedback on a correct pick should say why it is right, with a claim (DP13)")
    # DP14 phrase scan over everything the learner reads
    texts = [(nid, m.get("text", "")) for nid, d in nodes.items()
             for m in (d.get("say") or []) + ([d["sure_note"]] if isinstance(d.get("sure_note"), dict) else [])]
    texts += [("report", m.get("text", "")) for m in iter_report(mod.get("report"))]
    for where, t in texts:
        low = t.lower()
        for kind, phrases in BANNED.items():
            for ph in phrases:
                if ph in low:
                    (issues["errors"] if kind in BANNED_ERRORS else issues["warnings"]).append(
                        f"{where}: banned {kind} phrase '{ph}' (DP14)")
    # DP27 objectives are observable decisions
    for o in mod.get("objectives", []):
        if o.get("core") and re.match(r"(understand|know|be aware|appreciate)\b", o.get("text", "").strip().lower()):
            issues["warnings"].append(f"objective {o['id']}: phrase it as an observable decision, not 'understand/know' (DP27)")
    # DP11: the last segment needs at least one cold probe (no help option)
    last = mod["segments"][-1]["id"] if mod.get("segments") else None
    if last and not any(d.get("segment") == last and not any(c.get("kind") == "help" for c in d.get("choices") or [])
                        for d in probes.values()):
        issues["errors"].append(f"{last}: needs at least one probe without a hint option, for cold evidence (DP11)")
    n = max(1, len(probes))
    metrics.update({
        "key_longest_share": round(key_longest / n, 3),
        "key_position_max_share": round(max(key_pos.values(), default=0) / n, 3),
        "traps_per_probe_mean": round(sum(traps_per_probe) / n, 2),
        "probes_single_trap_share": round(sum(x == 1 for x in traps_per_probe) / n, 3),
        "retest_form_distinct_share": round(distinct / max(1, len(by_trap)), 3),
    })
    if metrics["key_longest_share"] > 0.4:
        issues["errors"].append(f"correct option is the longest in {metrics['key_longest_share']:.0%} of probes (max 40%, DP1)")
    if metrics["key_position_max_share"] > 0.5:
        issues["warnings"].append(f"correct option sits in one position in {metrics['key_position_max_share']:.0%} of probes (DP1)")

# ---------------------------------------------------------------- validate module

def validate_module(module_id, mod, bp, bank, require_report=False):
    issues = {"errors": [], "warnings": []}
    nodes = mod["nodes"]
    seg_type = {s["id"]: s["type"] for s in mod["segments"]}
    check_nodes(nodes, module_id, bank, bp, issues, seg_type)
    unver_nodes = issues.pop("_unverified_nodes", set())

    def resolve(t):
        if t not in nodes:
            issues["errors"].append(f"next {t!r} is not a node")
            return None
        return t

    g = edges(nodes, resolve)
    start = mod["start"]
    ends = [n for n, d in nodes.items() if d.get("end")]
    if start not in nodes:
        issues["errors"].append(f"start {start!r} is not a node")
        return issues, {}
    if not ends:
        issues["errors"].append("no end node")
    seen = reach(g, start)
    for n in nodes:
        if n not in seen:
            issues["errors"].append(f"{n}: unreachable from start")
    ok = can_reach(g, ends)
    for n in seen:
        if n not in ok:
            issues["errors"].append(f"{n}: cannot reach an end (dead end or trap loop)")
    core = reach(g, start, skip_kinds={"deeper"})
    for n in unver_nodes:
        if n in core and seg_type.get(nodes[n].get("segment")) != "traps":
            issues["errors"].append(f"{n}: unverified claim on the core path (move it behind a 'deeper' choice or into traps)")
    for o in mod.get("objectives", []):
        tagged = frozenset(n for n, d in nodes.items() if o["id"] in d.get("objectives", []))
        if not tagged:
            (issues["errors"] if o.get("core") else issues["warnings"]).append(f"objective {o['id']} never taught or tested")
            continue
        if o.get("core") and set(ends) & reach(g, start, avoid=tagged):
            issues["errors"].append(f"core objective {o['id']} can be skipped: a path reaches the end without it")
    offered = {}
    for nid, d in nodes.items():
        for c in d.get("choices") or []:
            if c.get("kind") == "trap":
                offered.setdefault(c.get("trap"), set()).add(nid)
    for t in mod.get("traps", []):
        n_probes = len(offered.get(t["id"], ()))
        if n_probes == 0:
            issues["errors"].append(f"trap {t['id']} is never offered as a choice")
        elif n_probes < 2:
            issues["errors"].append(f"trap {t['id']} is offered on only one probe (needs a later re-test in another form)")
        if t.get("error_type") not in ERROR_TYPES:
            issues["errors"].append(f"trap {t['id']}: error_type {t.get('error_type')!r} not in reference/traps.md")
    check_report(mod, issues, require_report)
    tr, loop = tell_run(nodes, g)
    lim = cfg("module", "max_tell_run", default=2)
    if loop:
        issues["errors"].append(f"{loop}: loop of non-interactive nodes")
    elif tr > lim:
        issues["errors"].append(f"{tr} non-interactive nodes in a row (max {lim})")
    lo, hi = cfg("module", "segments", default=[5, 8])
    if not lo <= len(mod["segments"]) <= hi:
        issues["warnings"].append(f"{len(mod['segments'])} segments (expected {lo}–{hi})")
    msgs = [m for d in nodes.values() for m in d.get("say") or []]
    wc = [words(m["text"]) for m in msgs if isinstance(m, dict) and "text" in m]
    interactive = [n for n, d in nodes.items() if len(d.get("choices") or []) >= 2]
    shortest, longest = path_lengths(g, start, set(ends))
    hy = {k for k, c in bank["claims"].items() if c.get("hy") and c["status"] == "verified"}
    cited = {c for c in mod["claims"] if "#" not in c}
    metrics = {
        "nodes": len(nodes), "segments": len(mod["segments"]),
        "probes": sum(d.get("role") == "probe" for d in nodes.values()),
        "interactivity": round(len(interactive) / max(1, len(nodes)), 3),
        "max_tell_run": tr, "shortest_path": shortest, "longest_path": longest,
        "words_per_message_mean": round(sum(wc) / max(1, len(wc)), 1), "words_per_message_max": max(wc, default=0),
        "claims_cited": len(cited), "claims_in_bank": len(bank["claims"]),
        "hy_coverage": round(len(hy & cited) / max(1, len(hy)), 3),
        "hy_missing": sorted(hy - cited, key=lambda k: int(k[1:])),
        "traps": len(mod.get("traps", [])),
        "trap_probes_mean": round(sum(len(v) for v in offered.values()) / max(1, len(offered)), 2),
        "cards": len(mod.get("cards", [])),
        "confidence_probes": sum(bool(d.get("ask_confidence")) for d in nodes.values()),
        "fast_lanes": sum(c.get("kind") == "skip" for d in nodes.values() for c in d.get("choices") or []),
    }
    lint_module(mod, issues, metrics)
    if metrics["hy_missing"]:
        issues["warnings"].append(f"high-yield claims not taught: {', '.join(metrics['hy_missing'])}")
    return issues, metrics


def cmd_validate(a):
    w = work(a.module)
    mod = read_json(Path(a.path) if a.path else w / "module.json")
    bp, bank = read_json(w / "blueprint.json"), load_bank(a.module)
    if mod is None or bp is None:
        die("need module.json and blueprint.json")
    issues, metrics = validate_module(a.module, mod, bp, bank, a.require_report)
    out = {"validated": now(), "errors": issues["errors"], "warnings": issues["warnings"], "metrics": metrics}
    if not a.path:
        write_json(w / "validation.json", out)
    print(json.dumps({"errors": len(issues["errors"]), "warnings": len(issues["warnings"]),
                      "first_errors": issues["errors"][:15], "metrics": {k: v for k, v in metrics.items()
                                                                         if k != "hy_missing"}}, indent=2))
    sys.exit(1 if issues["errors"] else 0)


# ---------------------------------------------------------------- score & best

def verifier_fails(w):
    p = w / "dialogue-verification.md"
    if not p.exists():
        return None
    return len(re.findall(r"\|\s*FAIL\s*\|", p.read_text(encoding="utf-8")))


def cmd_score(a):
    w = work(a.module)
    st = load_state(a.module)
    val = read_json(w / "validation.json", {})
    review = read_json(w / "review.json", {})
    sims = [read_json(p) for p in sorted((w / "sim").glob("*.json"))]
    m = val.get("metrics", {})
    j = float(review.get("weighted") or 0)
    sim_scores, headlines = [], {}
    mod_now = read_json(w / "module.json", {})
    for s in sims:
        tr = s.get("traps", {})
        fixed = sum(v == "fixed" for v in tr.values()) / max(1, len(tr)) if tr else 1.0
        cards = s.get("cards_answerable", 0) / max(1, s.get("cards_total", 0)) if s.get("cards_total") else 0.5
        sim_scores.append(0.4 * float(s.get("engagement", 3)) + 0.3 * 5 * fixed + 0.3 * 5 * cards)
        if s.get("path") and mod_now.get("report"):
            try:
                headlines[s.get("persona")] = render_report(mod_now, s["path"])["headline"]
            except (KeyError, IndexError, TypeError):
                headlines[s.get("persona")] = "broken-path"
    s_score = sum(sim_scores) / len(sim_scores) if sim_scores else 0
    parts = [min(1, m.get("interactivity", 0) / 0.6), m.get("hy_coverage", 0),
             1.0 if not val.get("errors") else 0.0,
             1.0 if (m.get("max_tell_run") or 99) <= cfg("module", "max_tell_run", default=2) else 0.0,
             # The report must tell learners apart: the strong sim and the misconceived sim should not get the same headline.
             1.0 if headlines.get("strong") and headlines.get("misconceived") and headlines["strong"] != headlines["misconceived"] else 0.0]
    m_score = 1 + 4 * sum(parts) / len(parts)
    composite = round(0.5 * j + 0.25 * s_score + 0.25 * m_score, 3)
    fails = verifier_fails(w)
    gated = bool(val.get("errors")) or not review  # knowledge-only: no fact-check gate
    card = read_json(w / "scorecard.json", {"rounds": [], "best": None})
    entry = {"round": st["round"], "at": now(), "judges": round(j, 3), "sims": round(s_score, 3),
             "metrics": round(m_score, 3), "composite": composite, "gated": gated,
             "validator_errors": len(val.get("errors", [])), "verifier_fails": fails,
             "weakest": review.get("weakest", []), "sim_headlines": headlines}
    card["rounds"] = [r for r in card["rounds"] if r["round"] != st["round"]] + [entry]
    best = card.get("best")
    improved = (not gated) and (best is None or composite >= best["composite"] + cfg("refine", "min_improvement", default=0.1)
                                or best["round"] == st["round"])
    if improved:
        card["best"] = {"round": st["round"], "composite": composite}
        dst = w / "best"
        if dst.exists():
            shutil.rmtree(dst)
        shutil.copytree(w / "segments", dst / "segments")
        shutil.copy(w / "module.json", dst / "module.json")
    write_json(w / "scorecard.json", card)
    print(json.dumps({"composite": composite, "gated": gated, "improved": improved,
                      "best": card["best"], "threshold": cfg("refine", "publish_threshold", default=4.0)}))


def cmd_restore(a):
    w = work(a.module)
    if not (w / "best" / "module.json").exists():
        die("no best snapshot")
    shutil.rmtree(w / "segments")
    shutil.copytree(w / "best" / "segments", w / "segments")
    shutil.copy(w / "best" / "module.json", w / "module.json")
    print("restored best round")


def cmd_publish(a):
    w = work(a.module)
    src = w / "best" / "module.json"
    if not src.exists():
        die("nothing to publish: no best round (every round was gated)")
    mod = read_json(src)
    card = read_json(w / "scorecard.json")
    best = card["best"]
    mod["status"] = "published" if best["composite"] >= cfg("refine", "publish_threshold", default=4.0) else "published-below-threshold"
    mod["quality"] = {"composite": best["composite"], "round": best["round"]}
    mod["built"] = today()
    write_json(MODULES / f"{a.module}.json", mod)
    write_index()
    print(f"published modules/{a.module}.json ({mod['status']}, composite {best['composite']})")


def cmd_clear(a):
    """Delete regenerable work: `variants S1 S2`, `sim`, or `blind S1`."""
    w = work(a.module)
    targets = [w / a.what / s for s in a.segments] if a.segments else [w / a.what]
    if a.what not in ("variants", "blind", "sim", "judging"):
        die("can only clear variants, blind, judging or sim")
    for t in targets:
        if a.what == "judging" and a.segments:
            for f in (w / "judging").glob(f"{t.name}-*.json"):
                f.unlink()
        elif t.exists():
            shutil.rmtree(t)
    print(f"cleared {a.what} {' '.join(a.segments)}".strip())


def cmd_archive_evidence(a):
    """Before a refresh: move evidence/<module>/ to evidence/<module>/_previous/."""
    src = EVIDENCE / a.module
    if not src.exists():
        print("no evidence to archive")
        return
    dst = src / "_previous"
    if dst.exists():
        shutil.rmtree(dst)
    dst.mkdir(parents=True)
    for f in src.iterdir():
        if f.name != "_previous":
            shutil.move(str(f), dst / f.name)
    print(f"archived to {dst.relative_to(ROOT)}")


def write_index():
    items = []
    for p in sorted(MODULES.glob("*/*.json")):
        m = read_json(p)
        items.append({"id": m["id"], "title": m.get("title"), "subject": m.get("subject"),
                      "status": m.get("status"), "version": m.get("version"), "built": m.get("built"),
                      "quality": m.get("quality"), "path": f"{m['id']}.json"})
    write_json(MODULES / "index.json", {"updated": now(), "modules": items})


# ---------------------------------------------------------------- status

def cmd_status(a):
    states = all_states()
    stats = read_json(stats_path(), {"by_type": {}})
    techs = read_techniques()
    lines = ["# Factory status", "", f"Updated {now()}. Written by `scripts/factory.py status`; do not edit.", ""]
    if (FACTORY / "STOP").exists():
        lines += ["**Stopped**: `factory/STOP` exists. Delete it to resume.", ""]
    lines += ["## Modules", "", "| module | stage | round | best | status |", "|---|---|---|---|---|"]
    for s in states:
        card = read_json(work(s["module"]) / "scorecard.json", {})
        best = (card.get("best") or {}).get("composite", "")
        flag = f"BLOCKED: {s['blocked']}" if s.get("blocked") else ("published" if s["stage"] == "done" else "in progress")
        lines.append(f"| {s['module']} | {s['stage']} | {s['round']} | {best} | {flag} |")
    known = {s["module"] for s in states}
    pending = [r for r in read_queue() if f"{r['subject']}/{slugify(r['topic'])}" not in known]
    lines += ["", f"## Queue ({len(pending)} waiting)", ""]
    lines += [f"- {r['priority']} · {r['subject']} · {r['topic']}" for r in pending[:15]]
    lines += ["", "## Technique leaderboard", "", "| segment type | technique | trials | win rate | mean judge score |", "|---|---|---|---|---|"]
    for typ in SEGMENT_TYPES:
        rows = stats["by_type"].get(typ, {})
        for t, r in sorted(rows.items(), key=lambda kv: -(kv[1]["wins"] / max(1, kv[1]["trials"]))):
            lines.append(f"| {typ} | {t} {techs.get(t, {}).get('name', '')} | {r['trials']} | "
                         f"{r['wins'] / max(1, r['trials']):.2f} | {r['score_sum'] / max(1, r['trials']):.2f} |")
    (FACTORY / "status.md").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


# ---------------------------------------------------------------- CLI

def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)

    def add(name, fn, help_, *args):
        sp = sub.add_parser(name, help=help_)
        for spec in args:
            sp.add_argument(*spec[0], **spec[1])
        sp.set_defaults(fn=fn)

    MOD = (["module"], {"help": "<subject>/<slug>"})
    add("next", cmd_next, "what should this tick do (JSON)")
    add("start", cmd_start, "create state for a queued topic",
        (["subject"], {}), (["topic"], {}), (["--slug"], {}), (["--force"], {"action": "store_true"}))
    add("advance", cmd_advance, "move a module to a stage", MOD, (["to"], {}),
        (["--note"], {}), (["--round"], {"type": int}))
    add("fail", cmd_fail, "record a failed stage attempt", MOD, (["--reason"], {"required": True}))
    add("unblock", cmd_unblock, "clear a block", MOD)
    add("bank", cmd_bank, "build claim-bank.json from the note", MOD)
    add("pick", cmd_pick, "choose competing techniques for a segment type",
        (["type"], {"choices": SEGMENT_TYPES}), (["--k"], {"type": int}),
        (["--seed"], {"default": "0"}), (["--require"], {"nargs": "*"}))
    add("blind", cmd_blind, "copy a segment's variants under shuffled labels", MOD, (["segment"], {}))
    add("record", cmd_record, "update technique stats after an edit decision", MOD, (["segment"], {}))
    add("check-segment", cmd_check_segment, "validate one segment file", MOD, (["path"], {}))
    add("assemble", cmd_assemble, "stitch segments into module.json", MOD)
    add("validate", cmd_validate, "validate module.json", MOD, (["--path"], {}),
        (["--require-report"], {"action": "store_true"}))
    add("render-report", cmd_render_report, "render the end-of-module report for a path file", MOD,
        (["path"], {"help": "JSON list of {node, choice, sure}, or a sim JSON with a path key"}),
        (["--module-file", "--path-module"], {"dest": "path_module"}))
    add("score", cmd_score, "score this round; snapshot it if best", MOD)
    add("restore", cmd_restore, "restore the best round's segments", MOD)
    add("publish", cmd_publish, "publish the best round to modules/", MOD)
    add("clear", cmd_clear, "delete regenerable work files", MOD,
        (["what"], {}), (["segments"], {"nargs": "*"}))
    add("archive-evidence", cmd_archive_evidence, "move old evidence aside before a refresh", MOD)
    add("experiment-done", cmd_experiment_done, "record that a design experiment ran", (["exp"], {}))
    add("status", cmd_status, "write factory/status.md")
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()

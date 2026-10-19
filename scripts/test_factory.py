#!/usr/bin/env python3
"""Tests for the deterministic parts of scripts/factory.py: graph validation and the report engine.

Run: python3 scripts/test_factory.py
"""

import copy
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import factory as F  # noqa: E402

BANK = {"claims": {"K1": {"text": "A is B.", "refs": ["1"], "status": "verified", "hy": True},
                   "K2": {"text": "C is D.", "refs": ["1"], "status": "verified", "hy": False},
                   "K3": {"text": "E maybe F.", "refs": ["2"], "status": "unverified", "hy": False}},
        "references": {"1": {"title": "t", "url": "u", "tier": 1}, "2": {"title": "t2", "url": "u2", "tier": 2}}}


def msg(text, *claims):
    return {"text": text, "claims": list(claims)}


def R(*keys):
    return {k: msg(f"{k} text") for k in keys}


def module():
    nodes = {
        "S1.q1": {"role": "probe", "segment": "S1", "objectives": ["O1"], "ask_confidence": True,
                  "say": [msg("Which is B?")],
                  "choices": [{"label": "A", "next": "S1.ok", "kind": "correct"},
                              {"label": "X", "next": "S1.t1", "kind": "trap", "trap": "TR1"},
                              {"label": "Hint", "next": "S1.h", "kind": "help"}]},
        "S1.h": {"role": "hint", "segment": "S1", "say": [msg("Think about A.")],
                 "choices": [{"label": "Try again", "next": "S1.q1", "kind": "retry"}]},
        "S1.t1": {"role": "feedback", "segment": "S1", "say": [msg("Tempting, but A is B.", "K1")],
                  "choices": [{"label": "Next", "next": "S2.q2", "kind": "continue"}]},
        "S1.ok": {"role": "feedback", "segment": "S1", "say": [msg("Yes: A is B.", "K1")],
                  "choices": [{"label": "Next", "next": "S2.q2", "kind": "continue"}]},
        "S2.q2": {"role": "probe", "segment": "S2", "objectives": ["O1", "O2"],
                  "say": [msg("A case. Which fits?")],
                  "choices": [{"label": "A again", "next": "S2.ok", "kind": "correct"},
                              {"label": "X again", "next": "S2.t1", "kind": "trap", "trap": "TR1"},
                              {"label": "D", "next": "S2.t2", "kind": "trap", "trap": "TR2"}]},
        "S2.t1": {"role": "feedback", "segment": "S2", "say": [msg("Still X: it is A.", "K1")],
                  "choices": [{"label": "Next", "next": "S2.q3", "kind": "continue"}]},
        "S2.t2": {"role": "feedback", "segment": "S2", "say": [msg("C is D, not this.", "K2")],
                  "choices": [{"label": "Next", "next": "S2.q3", "kind": "continue"}]},
        "S2.ok": {"role": "feedback", "segment": "S2", "say": [msg("Right.", "K1")],
                  "choices": [{"label": "Next", "next": "S2.q3", "kind": "continue"}]},
        "S2.q3": {"role": "probe", "segment": "S2", "objectives": ["O2"],
                  "say": [msg("Last one.")],
                  "choices": [{"label": "C", "next": "END", "kind": "correct"},
                              {"label": "Y", "next": "END", "kind": "trap", "trap": "TR2"}]},
        "END": {"role": "end", "end": True, "segment": "S2", "say": [msg("Done.")]},
    }
    objectives = [{"id": "O1", "kud": "know", "core": True, "text": "o1"},
                  {"id": "O2", "kud": "know", "core": True, "text": "o2"}]
    traps = [{"id": "TR1", "trap": "X is B", "error_type": "E1", "objectives": ["O1"]},
             {"id": "TR2", "trap": "D fits", "error_type": "E1", "objectives": ["O2"]}]
    report = {"headline": R("strong", "mixed", "weak"),
              "objectives": {o["id"]: R("secure", "shaky", "gap") for o in objectives},
              "traps": {t["id"]: R("avoided", "fell_recovered", "fell_open") for t in traps},
              "error_types": {"E1": msg("E1 pattern")},
              "calibration": R("overconfident", "underconfident", "calibrated"),
              "help": R("hints_heavy", "hints_none", "hinted_only"), "next_steps": R("gap", "clear")}
    return {"id": "x/y", "start": "S1.q1", "nodes": nodes, "objectives": objectives, "traps": traps,
            "segments": [{"id": "S1", "type": "retrieve"}, {"id": "S2", "type": "clinical"}],
            "claims": {"K1": BANK["claims"]["K1"], "K2": BANK["claims"]["K2"]}, "cards": [], "report": report}


BP = {"objectives": module()["objectives"], "traps": module()["traps"],
      "segments": [{"id": "S1", "type": "retrieve"}, {"id": "S2", "type": "clinical"}]}


class Validate(unittest.TestCase):
    def errors(self, mod):
        issues, _ = F.validate_module("x/y", mod, BP, BANK, require_report=True)
        return issues["errors"]

    def test_clean(self):
        self.assertEqual(self.errors(module()), [])

    def test_free_text_field_rejected(self):
        m = module()
        m["nodes"]["S1.q1"]["input"] = "text"
        self.assertTrue(any("unknown field 'input'" in e for e in self.errors(m)))

    def test_probe_needs_trap(self):
        m = module()
        m["nodes"]["S2.q3"]["choices"][1] = {"label": "Y", "next": "END", "kind": "partial"}
        self.assertTrue(any("probe without a trap" in e for e in self.errors(m)))

    def test_trap_needs_retest(self):
        m = module()
        m["nodes"]["S2.q2"]["choices"][1] = {"label": "X again", "next": "S2.t1", "kind": "partial"}
        self.assertTrue(any("TR1 is offered on only one probe" in e for e in self.errors(m)))

    def test_report_completeness(self):
        m = module()
        del m["report"]["traps"]["TR2"]["fell_open"]
        self.assertTrue(any("report.traps.TR2.fell_open" in e for e in self.errors(m)))

    def test_unverified_needs_flag(self):
        m = module()
        m["nodes"]["S1.ok"]["say"].append(msg("Maybe F.", "K3"))
        self.assertTrue(any("without flag" in e for e in self.errors(m)))

    def test_core_objective_on_every_path(self):
        m = module()
        m["nodes"]["S2.q2"]["objectives"] = ["O1"]
        m["nodes"]["S2.ok"]["choices"][0]["next"] = "END"  # a right answer at q2 now skips q3, O2's only probe
        self.assertTrue(any("core objective O2 can be skipped" in e for e in self.errors(m)))

    def test_duplicate_labels(self):
        m = module()
        m["nodes"]["S1.q1"]["choices"][1]["label"] = "A"
        self.assertTrue(any("share a label" in e for e in self.errors(m)))


class Report(unittest.TestCase):
    def test_all_correct(self):
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 0, "sure": True}, {"node": "S1.ok", "choice": 0},
                                         {"node": "S2.q2", "choice": 0}, {"node": "S2.ok", "choice": 0},
                                         {"node": "S2.q3", "choice": 0}])
        self.assertEqual(rep["headline"], "strong")
        self.assertEqual(rep["traps"], {"TR1": "avoided", "TR2": "avoided"})
        self.assertEqual(rep["objectives"], {"O1": "secure", "O2": "secure"})

    def test_fell_then_recovered(self):
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 1, "sure": True}, {"node": "S1.t1", "choice": 0},
                                         {"node": "S2.q2", "choice": 0}, {"node": "S2.ok", "choice": 0},
                                         {"node": "S2.q3", "choice": 0}])
        self.assertEqual(rep["traps"]["TR1"], "fell_recovered")
        self.assertEqual(rep["objectives"]["O1"], "shaky")  # half wrong at first, but the latest answer is right

    def test_fell_open_and_error_profile(self):
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 1, "sure": True}, {"node": "S1.t1", "choice": 0},
                                         {"node": "S2.q2", "choice": 1}, {"node": "S2.t1", "choice": 0},
                                         {"node": "S2.q3", "choice": 1}])
        self.assertEqual(rep["traps"], {"TR1": "fell_open", "TR2": "fell_open"})
        self.assertEqual(rep["headline"], "weak")
        self.assertIn("E1 pattern", rep["texts"])

    def test_hints_counted(self):
        path = [{"node": "S1.q1", "choice": 2}, {"node": "S1.h", "choice": 0}] * 3 + \
               [{"node": "S1.q1", "choice": 0, "sure": False}, {"node": "S1.ok", "choice": 0},
                {"node": "S2.q2", "choice": 0}, {"node": "S2.ok", "choice": 0}, {"node": "S2.q3", "choice": 0}]
        rep = F.render_report(module(), path)
        self.assertEqual(rep["hints"], 3)
        self.assertIn("hints_heavy text", rep["texts"])

    def test_confident_errors_first(self):
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 0, "sure": False}, {"node": "S1.ok", "choice": 0},
                                         {"node": "S2.q2", "choice": 2}, {"node": "S2.t2", "choice": 0},
                                         {"node": "S2.q3", "choice": 1}])
        self.assertEqual(rep["confident_errors"], [])
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 1, "sure": True}, {"node": "S1.t1", "choice": 0},
                                         {"node": "S2.q2", "choice": 2}, {"node": "S2.t2", "choice": 0},
                                         {"node": "S2.q3", "choice": 1}])
        self.assertEqual(rep["confident_errors"], ["TR1"])

    def test_hinted_only(self):
        rep = F.render_report(module(), [{"node": "S1.q1", "choice": 2}, {"node": "S1.h", "choice": 0},
                                         {"node": "S1.q1", "choice": 0, "sure": True}, {"node": "S1.ok", "choice": 0},
                                         {"node": "S2.q2", "choice": 2}, {"node": "S2.t2", "choice": 0},
                                         {"node": "S2.q3", "choice": 1}])
        self.assertEqual(rep["hinted_only"], ["O1"])
        self.assertIn("hinted_only text", rep["texts"])


class Lints(unittest.TestCase):
    def errors(self, mod):
        issues, _ = F.validate_module("x/y", mod, BP, BANK, require_report=True)
        return issues

    def test_all_of_the_above(self):
        m = module()
        m["nodes"]["S2.q3"]["choices"][1]["label"] = "All of the above"
        self.assertTrue(any("DP1" in e for e in self.errors(m)["errors"]))

    def test_same_trap_twice(self):
        m = module()
        m["nodes"]["S2.q2"]["choices"][2]["trap"] = "TR1"
        self.assertTrue(any("same trap" in e for e in self.errors(m)["warnings"]))

    def test_scolding_phrase(self):
        m = module()
        m["nodes"]["S1.t1"]["say"][0]["text"] = "Wrong! A is B."
        self.assertTrue(any("DP14" in e for e in self.errors(m)["errors"]))

    def test_cold_probe_required(self):
        m = module()
        m["nodes"]["S2.q3"]["choices"].append({"label": "Hint", "next": "S1.h", "kind": "help"})
        m["nodes"]["S2.q2"]["choices"].append({"label": "Hint", "next": "S1.h", "kind": "help"})
        self.assertTrue(any("DP11" in e for e in self.errors(m)["errors"]))


class PlayerParity(unittest.TestCase):
    """The player's JS report engine must agree with render_report on the same paths."""

    PATHS = [
        [{"node": "S1.q1", "choice": 0, "sure": True}, {"node": "S1.ok", "choice": 0}, {"node": "S2.q2", "choice": 0},
         {"node": "S2.ok", "choice": 0}, {"node": "S2.q3", "choice": 0}],
        [{"node": "S1.q1", "choice": 1, "sure": True}, {"node": "S1.t1", "choice": 0}, {"node": "S2.q2", "choice": 1},
         {"node": "S2.t1", "choice": 0}, {"node": "S2.q3", "choice": 1}],
        [{"node": "S1.q1", "choice": 2}, {"node": "S1.h", "choice": 0}, {"node": "S1.q1", "choice": 0, "sure": False},
         {"node": "S1.ok", "choice": 0}, {"node": "S2.q2", "choice": 2}, {"node": "S2.t2", "choice": 0},
         {"node": "S2.q3", "choice": 0}],
    ]
    KEYS = ["headline", "objectives", "traps", "calibration", "sure_wrong", "guess_right", "hints", "fast_lane",
            "confident_errors", "hinted_only", "cold_right", "cold_total", "card_order"]

    def test_parity(self):
        import json, shutil, subprocess
        if not shutil.which("node"):
            self.skipTest("node not installed")
        html = (Path(__file__).resolve().parent.parent / "player" / "index.html").read_text(encoding="utf-8")
        js = html.split("<script>")[1].split("</script>")[0]
        start = js.index("function computeReport()")
        engine = js[start:js.index("function rtext(")]
        mod = module()
        mod["cards"] = [{"q": "q", "a": "a", "claims": ["K1"], "objective": "O2"},
                        {"q": "q", "a": "a", "claims": ["K1"], "objective": "O1"}]
        for path in self.PATHS:
            hist = [{"at": st["node"], "choice": st["choice"], "sure": st.get("sure")} for st in path]
            prog = (f"const M = {json.dumps(mod)}; const S = {{hist: {json.dumps(hist)}}};\n{engine}\n"
                    "const r = computeReport(); delete r.steps; console.log(JSON.stringify(r));")
            out = json.loads(subprocess.run(["node", "-e", prog], capture_output=True, text=True, check=True).stdout)
            py = F.render_report(mod, path)
            for k in self.KEYS:
                self.assertEqual(out.get(k), py.get(k), f"{k} differs on path {path[0]}")


if __name__ == "__main__":
    unittest.main(verbosity=1)

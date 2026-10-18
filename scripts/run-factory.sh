#!/usr/bin/env bash
# Run the LORE factory unattended: one Claude Code session per tick.
#
#   scripts/run-factory.sh [ticks] [--push]
#
# ticks   how many ticks to run (default 20). Each tick advances one module by one stage.
# --push  push after every tick's commit, so a cloud container can die without losing work.
#
# Stop any time: touch factory/STOP (the loop exits before the next tick).
# Set LORE_MODEL to choose the orchestrator's model (agents use the models in CLAUDE.md).
set -uo pipefail
cd "$(dirname "$0")/.."

TICKS="${1:-20}"
PUSH="${2:-}"
LOCK="factory/.lock"

if ! mkdir "$LOCK" 2>/dev/null; then
  echo "Another factory loop holds $LOCK. If none is running, remove it: rmdir $LOCK"
  exit 1
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

MODEL_ARGS=()
[ -n "${LORE_MODEL:-}" ] && MODEL_ARGS=(--model "$LORE_MODEL")

for ((i = 1; i <= TICKS; i++)); do
  if [ -f factory/STOP ]; then echo "factory/STOP found; stopping."; break; fi
  NEXT="$(python3 scripts/factory.py next)"
  echo "[$(date '+%F %T')] tick $i/$TICKS: $NEXT"
  case "$NEXT" in *'"action": "stop"'*) break ;; esac

  {
    echo "===== tick $i $(date '+%F %T') $NEXT"
    claude -p "Run one tick of the LORE factory: follow .claude/skills/lore-factory/SKILL.md exactly." \
      --permission-mode acceptEdits "${MODEL_ARGS[@]}"
  } >> factory/ticks.log 2>&1 || echo "  tick $i: claude exited with an error (see factory/ticks.log)"

  python3 scripts/factory.py status > /dev/null
  git add -A
  if git commit -q -m "factory: $(tail -n 1 factory/log.md | sed 's/^- //' | cut -c1-100)"; then
    echo "  committed: $(git log -1 --format=%s)"
    if [ "$PUSH" = "--push" ]; then
      git push -q -u origin HEAD || echo "  push failed; will retry next tick"
    fi
  fi
done

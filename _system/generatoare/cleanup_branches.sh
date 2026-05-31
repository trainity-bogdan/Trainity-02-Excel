#!/usr/bin/env bash
# cleanup_branches.sh - sterge toate branch-urile in afara de `main`.
#
# SAFE BY DEFAULT: fara --force ruleaza DRY-RUN (doar listeaza ce ar sterge).
# `main` este PROTEJAT mereu. Inainte de a sterge branch-ul curent, comuta pe main.
#
# Uz:
#   bash _system/generatoare/cleanup_branches.sh              # dry-run, local
#   bash _system/generatoare/cleanup_branches.sh --remote     # dry-run, remote (origin)
#   bash _system/generatoare/cleanup_branches.sh --all        # dry-run, local + remote
#   bash _system/generatoare/cleanup_branches.sh --all --force # STERGE efectiv
#
# Note:
#  - Branch-urile merse in main sunt recuperabile via reflog/SHA; cele NEMERSE se pierd.
#    Scriptul refuza sa stearga local branch-uri nemerse in main decat cu --force-unmerged.
#  - Pe remote, `git branch -D` echivalent = `git push origin --delete`.

set -euo pipefail

PROTECTED="main"
MODE="local"      # local | remote | all
FORCE=0           # 0 = dry-run, 1 = executa
FORCE_UNMERGED=0  # permite stergerea branch-urilor locale nemerse in main

for arg in "$@"; do
  case "$arg" in
    --local)  MODE="local" ;;
    --remote) MODE="remote" ;;
    --all)    MODE="all" ;;
    --force)  FORCE=1 ;;
    --force-unmerged) FORCE_UNMERGED=1 ;;
    -h|--help) sed -n '2,20p' "$0"; exit 0 ;;
    *) echo "arg necunoscut: $arg (vezi --help)"; exit 1 ;;
  esac
done

say() { printf '%s\n' "$*"; }
do_cmd() {
  if [ "$FORCE" -eq 1 ]; then
    eval "$1"
  else
    say "  [dry-run] $1"
  fi
}

# Comuta pe main daca esti pe alt branch (ca sa-l poti sterge local)
current="$(git rev-parse --abbrev-ref HEAD)"
if [ "$current" != "$PROTECTED" ]; then
  say "Esti pe '$current'. Comut pe '$PROTECTED'..."
  if [ "$FORCE" -eq 1 ]; then git checkout "$PROTECTED" >/dev/null 2>&1 || { say "Nu pot comuta pe $PROTECTED (working tree murdar?)"; exit 1; }; fi
fi

if [ "$MODE" = "local" ] || [ "$MODE" = "all" ]; then
  say "=== LOCAL (in afara de $PROTECTED) ==="
  git for-each-ref --format='%(refname:short)' refs/heads/ \
    | grep -vx "$PROTECTED" \
    | while IFS= read -r b; do
        [ -z "$b" ] && continue
        if [ "$FORCE_UNMERGED" -eq 1 ]; then
          do_cmd "git branch -D '$b'"
        else
          do_cmd "git branch -d '$b'"   # -d esueaza daca nu e merge in HEAD/main
        fi
      done
fi

if [ "$MODE" = "remote" ] || [ "$MODE" = "all" ]; then
  say "=== REMOTE origin (in afara de $PROTECTED) ==="
  git ls-remote --heads origin | awk '{print $2}' | sed 's#refs/heads/##' \
    | grep -vx "$PROTECTED" \
    | while IFS= read -r b; do
        [ -z "$b" ] && continue
        do_cmd "git push origin --delete '$b'"
      done
fi

if [ "$FORCE" -eq 0 ]; then
  say ""
  say ">>> A FOST DRY-RUN. Adauga --force ca sa stergi efectiv."
fi

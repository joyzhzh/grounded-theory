#!/usr/bin/env bash
# Preflight for the external study vault pointer. Adapted from
# joyzhzh/evidence-first-deep-research-v2@fa6cc2e2f93136d2d7b5d29a3b5d5b3e7d445e1d
# scripts/doctor.sh (the pinned protocol revision); this repository installs no
# Scout skill, so that check is omitted and a no-.git-inside-the-vault check is added.
set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
pointer="$repo_root/.vault-root"

if [[ ! -f "$pointer" ]]; then
  echo "SETUP NEEDED: copy .vault-root.example to .vault-root and set this machine's absolute vault path."
  exit 1
fi

raw="$(sed -n '1p' "$pointer" | tr -d '\r')"
vault_root="$(printf '%s' "$raw" | sed -E 's/^[[:space:]]+//; s/[[:space:]]+$//')"
nonempty="$(grep -c -v -E '^[[:space:]]*$' "$pointer" || true)"

if (( nonempty != 1 )); then
  echo "INVALID: .vault-root must contain exactly one line, the absolute vault path (found $nonempty non-empty lines)."
  exit 1
fi

if [[ "$vault_root" == "~"* ]]; then
  echo "INVALID: .vault-root must be an absolute path; ~ is not expanded. Got: $raw"
  exit 1
fi

if [[ -z "$vault_root" || "$vault_root" != /* ]]; then
  echo "INVALID: .vault-root must contain one absolute path. Got: '$raw'"
  exit 1
fi

if [[ ! -d "$vault_root" ]]; then
  echo "UNAVAILABLE: vault directory does not exist or is not mounted: $vault_root"
  exit 1
fi

vault_root_canon="$(cd "$vault_root" && pwd -P)"
repo_root_canon="$(cd "$repo_root" && pwd -P)"

case "$vault_root_canon/" in
  "$repo_root_canon"/*)
    echo "INVALID: the study vault must be outside the Git repository (resolves to $vault_root_canon)."
    exit 1
    ;;
esac

case "$repo_root_canon/" in
  "$vault_root_canon"/*)
    echo "INVALID: the Git repository must not live inside the study vault ($repo_root_canon is under $vault_root_canon)."
    exit 1
    ;;
esac

if [[ -e "$vault_root_canon/.git" ]]; then
  echo "INVALID: the study vault must not contain a Git repository (.git found in $vault_root_canon)."
  exit 1
fi

if git -C "$repo_root" ls-files --error-unmatch .vault-root >/dev/null 2>&1; then
  echo "INVALID: .vault-root is tracked; remove it from the Git index before continuing."
  exit 1
fi

echo "PASS: .vault-root resolves to $vault_root_canon, outside this repository and untracked."

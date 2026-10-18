#!/usr/bin/env bash
# Clone or update every repo in repos.txt into design-refinement/repos/ (not committed:
# the repos keep their own licences; we commit only our analysis and what we apply).
set -uo pipefail
cd "$(dirname "$0")"
mkdir -p repos
grep -v '^\s*#' repos.txt | awk 'NF {print $1}' | while read -r slug; do
  dir="repos/${slug//\//__}"
  if [ -d "$dir/.git" ]; then git -C "$dir" pull -q --ff-only && echo "updated $slug"
  else git clone -q --depth 1 "https://github.com/$slug.git" "$dir" && echo "cloned  $slug" || echo "FAILED  $slug"
  fi
done

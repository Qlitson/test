#!/usr/bin/env bash

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"
SOURCE_DIR="${REPO_ROOT}/.agents/skills"
TARGET_DIR="${HOME}/.agents/skills"

if [[ ! -d "${SOURCE_DIR}" ]]; then
  echo "Source skill directory not found: ${SOURCE_DIR}" >&2
  exit 1
fi

mkdir -p "${TARGET_DIR}"

installed=0

for skill_dir in "${SOURCE_DIR}"/*; do
  if [[ -d "${skill_dir}" && -f "${skill_dir}/SKILL.md" ]]; then
    skill_name="$(basename "${skill_dir}")"
    rm -rf "${TARGET_DIR}/${skill_name}"
    cp -R "${skill_dir}" "${TARGET_DIR}/${skill_name}"
    echo "Installed ${skill_name} -> ${TARGET_DIR}/${skill_name}"
    installed=$((installed + 1))
  fi
done

if [[ "${installed}" -eq 0 ]]; then
  echo "No skills found in ${SOURCE_DIR}" >&2
  exit 1
fi

echo "Installed ${installed} skill(s) into ${TARGET_DIR}"

#!/usr/bin/env bash
set -e

echo "1) Actualizando CHANGELOG.md desde commits..."
conventional-changelog -p angular -i CHANGELOG.md -s

echo "2) Regenerando TOC en README.md y docs/guia_desarrollo.md..."
markdown-toc -i README.md -o README.md
markdown-toc -i docs/guia_desarrollo.md -o docs/guia_desarrollo.md

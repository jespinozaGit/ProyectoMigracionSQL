@echo off
echo 1) Actualizando CHANGELOG.md desde commits...
conventional-changelog -p angular -i CHANGELOG.md -s

echo 2) Regenerando TOC en README.md y docs/guia_desarrollo.md...
markdown-toc -i README.md
markdown-toc -i docs/guia_desarrollo.md

echo.
echo Listo. Haz commit de los cambios:
echo   git add CHANGELOG.md README.md docs/guia_desarrollo.md
echo   git commit -m "docs: actualización automática de docs y TOC"
pause
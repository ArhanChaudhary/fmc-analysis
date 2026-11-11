#!/bin/bash
# Build the public site (GitHub Pages, see .github/workflows/pages.yml): the three reports as HTML pages
# with a shared navigation bar and a table of contents per page, plus the Markdown sources.
# Needs pandoc.
# usage: scripts/build-pages.sh OUTPUT_DIRECTORY
set -euo pipefail
cd "$(dirname "$0")/.."
output=${1:?usage: scripts/build-pages.sh OUTPUT_DIRECTORY}
if [ -e "$output" ]; then
    echo "output already exists: $output (choose a new directory)" >&2
    exit 2
fi
mkdir -p "$output"

# render SOURCE.md PAGE.html NAV-FLAG
# The first heading of each report becomes the page title; the other headings keep the ids GitHub gives
# them, which is what the links inside the reports use.
render() {
    pandoc --from gfm --to html5 --standalone --shift-heading-level-by=-1 \
        --toc --toc-depth=2 --template site/template.html --variable "$3" \
        --output "$output/$2" "$1"
}
render report/WRITEUP.md index.html is-writeup
render report/EXAMPLES.md examples.html is-examples
render report/BUGS.md errata.html is-errata

# every in-page link must have a target (a broken one only shows when somebody clicks it)
for page in index.html examples.html errata.html; do
    for anchor in $(grep -o 'href="#[^"]*"' "$output/$page" | sed 's/href="#\(.*\)"/\1/' | sort -u); do
        grep -q "id=\"$anchor\"" "$output/$page" || { echo "build-pages: $page links to #$anchor, which does not exist" >&2; exit 1; }
    done
done

# on the site, mentions of the examples file are links to it
sed -i 's|the examples file|<a href="examples.html">the examples file</a>|g' "$output/index.html"

cp site/style.css "$output/"
cp report/WRITEUP.md report/EXAMPLES.md report/BUGS.md "$output/"
# (GitHub Pages: no Jekyll processing)
touch "$output/.nojekyll"
printf 'Pages site: %s\n' "$output"

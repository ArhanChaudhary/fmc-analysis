#!/bin/bash
# Build the public site (GitHub Pages, see .github/workflows/pages.yml): a front page that lists the
# case studies (site/index.md), and for every study folder with a report/WRITEUP.md its reports as HTML
# pages with a shared navigation bar and a table of contents per page, plus the Markdown sources.
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

# render SOURCE.md PAGE.html ROOT [more pandoc options]
# The first heading of a page becomes its title; the other headings keep the ids GitHub gives them,
# which is what the links inside the reports use.  ROOT is the way from the page to the site root.
render() {
    local source=$1 page=$2 root=$3
    shift 3
    pandoc --from gfm --to html5 --standalone --shift-heading-level-by=-1 --toc --toc-depth=2 \
        --lua-filter site/tables.lua --template site/template.html --variable "root=$root" "$@" \
        --output "$output/$page" "$source"
    # every in-page link must have a target (a broken one only shows when somebody clicks it)
    local anchor
    for anchor in $(grep -o 'href="#[^"]*"' "$output/$page" | sed 's/href="#\(.*\)"/\1/' | sort -u); do
        grep -q "id=\"$anchor\"" "$output/$page" || { echo "build-pages: $page links to #$anchor, which does not exist" >&2; exit 1; }
    done
}

render site/index.md index.html ./ --variable is-home

for writeup in */report/WRITEUP.md; do
    study=${writeup%%/*}
    [ -L "$study" ] && continue
    mkdir -p "$output/$study"
    pages=()
    [ -f "$study/report/EXAMPLES.md" ] && pages+=(--variable has-examples)
    [ -f "$study/report/BUGS.md" ] && pages+=(--variable has-errata)
    render "$study/report/WRITEUP.md" "$study/index.html" ../ --variable study "${pages[@]}" --variable is-writeup
    cp "$study/report/WRITEUP.md" "$output/$study/"
    if [ -f "$study/report/EXAMPLES.md" ]; then
        render "$study/report/EXAMPLES.md" "$study/examples.html" ../ --variable study "${pages[@]}" --variable is-examples
        cp "$study/report/EXAMPLES.md" "$output/$study/"
        # on the site, mentions of the examples file are links to it
        sed -i 's|the examples file|<a href="examples.html">the examples file</a>|g' "$output/$study/index.html"
    fi
    if [ -f "$study/report/BUGS.md" ]; then
        render "$study/report/BUGS.md" "$study/errata.html" ../ --variable study "${pages[@]}" --variable is-errata
        cp "$study/report/BUGS.md" "$output/$study/"
    fi
    # every study must be reachable from the front page
    grep -q "href=\"$study/\"" "$output/index.html" || { echo "build-pages: site/index.md does not link to $study/" >&2; exit 1; }
done

cp site/style.css "$output/"
# (GitHub Pages: no Jekyll processing)
touch "$output/.nojekyll"
printf 'Pages site: %s\n' "$output"

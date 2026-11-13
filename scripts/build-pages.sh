#!/bin/bash
# Build the public site (GitHub Pages, see .github/workflows/pages.yml): a front page that lists the
# case studies and the reference tables (site/index.md), for every study folder with a report/WRITEUP.md its reports
# as HTML pages with a shared navigation bar and a table of contents per page, plus the Markdown sources, and one
# page per reference table (tables/*.md).
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
cssver=$(sha1sum site/style.css | cut -c1-10)
warnings=$(mktemp)
trap 'rm -f "$warnings" "$warnings.page"' EXIT

# render SOURCE.md PAGE.html ROOT [more pandoc options]
# The first heading of a page becomes its title; the other headings keep the ids GitHub gives them,
# which is what the links inside the reports use.  ROOT is the way from the page to the site root.
render() {
    local source=$1 page=$2 root=$3
    shift 3
    # pandoc's messages, with the warnings of site/tables.lua, go to the terminal and to $warnings (counted at the end)
    pandoc --from gfm+tex_math_dollars --to html5 --katex=https://cdn.jsdelivr.net/npm/katex@0.16.11/dist/ --standalone --shift-heading-level-by=-1 --toc --toc-depth=2 \
        --lua-filter site/tables.lua --template site/template.html --variable "root=$root" --variable "cssver=$cssver" "$@" \
        --output "$output/$page" "$source" 2>"$warnings.page" || { cat "$warnings.page" >&2; exit 1; }
    cat "$warnings.page" >&2
    cat "$warnings.page" >> "$warnings"
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
    # a study folder with a file named UNLISTED is built but not linked from the front page, and asks
    # search engines not to index it: reachable only by its address
    [ -f "$study/UNLISTED" ] && pages+=(--variable noindex)
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
    # every study must be reachable from the front page, and an unlisted one must not be
    if [ -f "$study/UNLISTED" ]; then
        if grep -q "href=\"$study/\"" "$output/index.html"; then echo "build-pages: $study/ is UNLISTED but site/index.md links to it" >&2; exit 1; fi
    else
        grep -q "href=\"$study/\"" "$output/index.html" || { echo "build-pages: site/index.md does not link to $study/" >&2; exit 1; }
    fi
done

# reference tables: single pages under tables/, each too small for a study, listed on the front page
if compgen -G "tables/*.md" > /dev/null; then
    mkdir -p "$output/tables"
    for source in tables/*.md; do
        name=$(basename "$source" .md)
        render "$source" "tables/$name.html" ../ --variable is-table
        cp "$source" "$output/tables/"
        grep -q "href=\"tables/$name.html\"" "$output/index.html" || { echo "build-pages: site/index.md does not link to tables/$name.html" >&2; exit 1; }
    done
fi

# decision cards: one page of in-attempt questions answered from the studies' data (cards/decision-cards.md, written by
# cards/src/build.py), linked from the front page
if [ -f cards/decision-cards.md ]; then
    render cards/decision-cards.md decision-cards.html ./
    cp cards/decision-cards.md "$output/"
    grep -q 'href="decision-cards.html"' "$output/index.html" || { echo "build-pages: site/index.md does not link to decision-cards.html" >&2; exit 1; }
fi

# search: a page with the box (site/search.md, site/search.js) and an index of every listed page, section by section
# (scripts/search-index.py; unlisted studies stay out of it, so the index can't lead to them)
render site/search.md search.html ./ --variable is-home --variable is-search
cp site/search.js "$output/"
listed=()
for writeup in */report/WRITEUP.md; do
    study=${writeup%%/*}
    [ -L "$study" ] || [ -f "$study/UNLISTED" ] || listed+=("$study")
done
python3 scripts/search-index.py "$output" "${listed[@]}"

cp site/style.css "$output/"
# a table cell left empty after the row's first filled cell shows a dash (site/tables.lua); that is right for a
# value that doesn't apply, wrong for one a writer lost, so every such table is listed above
dashed=$(grep -c '^tables.lua: warning:' "$warnings" || true)
if [ "$dashed" -gt 0 ]; then
    echo "build-pages: warning: $dashed tables show a dash in an empty cell (listed above as 'tables.lua: warning'); check new ones against their writer" >&2
fi
# (GitHub Pages: no Jekyll processing)
touch "$output/.nojekyll"
printf 'Pages site: %s\n' "$output"

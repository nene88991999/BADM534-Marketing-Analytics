# Building the Lectures

`source/sessions.json` contains the projected content and substantive presenter notes. `theme.tex` supplies the shared Beamer format. Analytical figures are included directly from `../06_Lecture_Notes/figures/`; original artistic images are in `assets/`.

## Requirements and Commands

Use Python 3, `pypdf`, and a XeLaTeX-compatible Tectonic installation. Tectonic may download TeX packages on the first run. Building executes the local authoring script and TeX sources, not the reference notebooks in the resource library.

From the repository root:

```sh
python3 Lectures/build_slides.py --tectonic /path/to/tectonic
```

The command writes 15 session PDFs, editable LaTeX files, complete Markdown companions, and a combined PDF with session bookmarks. Intermediate products are under ignored `Lectures/build/`.

```sh
python3 Lectures/build_slides.py --sources-only
python3 Lectures/build_slides.py --tectonic /path/to/tectonic --only 14
python3 Lectures/build_slides.py --tectonic /path/to/tectonic --only 14 --presenter
```

Presenter mode writes a two-screen PDF to the selected session's build directory. The public deck remains the single-screen version. Rebuild the full collection after individual edits to refresh the combined PDF.

## Calculations and Companions

```sh
python3 03_Data_and_Code/Lecture_Examples/session_examples.py all
python3 03_Data_and_Code/Lecture_Examples/retention_welfare.py
python3 scripts/check_lecture_code.py
```

The small examples use only Python's standard library. They cover the projected calculations, including an independent grid check for budget allocation and enumeration of recommendation lists. The retention example writes a separate aggregate CSV and JSON. Empirical cases retain their complete programs, environments, and verification records in the linked data folders and module notes.

## Rendering and Review

Render PDFs with Poppler, inspect every page, and review compilation warnings before publication. Check code and equation readability, chart labels, table widths, and text near the orange rules. Check presenter mode separately. Page counts must agree with the content source, and every local link in a companion must resolve. Compilation verifies TeX execution; it does not establish the validity of an empirical interpretation.

The [verification record](verification.json) records the November 2, 2026 build, visual review, calculation checks, and execution scope.

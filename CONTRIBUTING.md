# Adding and Updating Course Materials

## Choose a Destination

Put a released syllabus in `02_Syllabus`, selected teaching data in `03_Data`, assignment briefs in `04_Assignments`, slides in `05_Slides`, written notes in `06_Lecture_Notes`, and course-tested code in `07_Labs`. Keep external background sources in `01_Resources`. Use `08_Wiki` for the later HTML site.

Use a stable module prefix, for example `M03_Regression_Notes.md`. For an assignment, use a dedicated folder such as `04_Assignments/A01_Customer_Analysis` containing `README.md`, the brief, rubric, and permitted starter files. These names are examples, not released assignments.

## Make Every Addition Readable by LLMs

1. Add a Markdown companion next to each PDF or slide deck. Include the title, module, date/version, status, key concepts, full requirements when relevant, and links to the original.
2. Preserve mathematical definitions, tables, chart descriptions, and page or slide references. Label a short summary as a summary; it cannot silently replace the complete assignment rules.
3. Give each dataset a dictionary with units, missing-value codes, observation unit, timing, source, license, and important limitations.
4. Give each lab a README with its environment, data paths, run command, expected checks, and execution status.
5. Add the file to the folder README. When releasing authoritative material, update the appropriate pointer in `course.json` and its status.
6. Add selected current Markdown companions to `llm_context_paths` in `course.json`, then run `python3 scripts/build_llm_context.py`.

Use [the templates](09_Templates/README.md) to begin. Replace placeholders explicitly; do not leave an unfinished template labeled as a released document.

## Publish an Update

Dropbox synchronization saves files to Dropbox. GitHub changes require a reviewed Git commit and push. From a local Git checkout authenticated to this repository:

```sh
python3 scripts/build_llm_context.py
git status --short
git diff --stat
git diff
# Stage the specific files you reviewed, for example:
git add 02_Syllabus/README.md 02_Syllabus/Current_Syllabus.md course.json llms-full.txt
git diff --cached --stat
git diff --cached
git commit -m "Add current course syllabus"
git push origin main
```

The example assumes `Current_Syllabus.md` exists and Git has been initialized and connected to the repository. GitHub's web upload interface is another option for occasional files. Keep local and remote changes reconciled before editing from both places. No automatic upload watcher is configured.

Before a student release, exclude private student information and answer keys, check the AI policy and assignment version, and review rights for redistributed sources. Before public wiki hosting, select content individually from the instructor research library. Some downloaded readings permit personal use only; link to those sources instead of republishing the files.

## Catalog Maintenance

The two resource catalogs were assembled separately and overlap. Preserve both until a deliberate reconciliation. Their IDs have different formats. Use a catalog path plus resource ID in machine-readable references. The curated library's maintenance instructions are in [01_Resources/_maintenance/README.md](01_Resources/_maintenance/README.md); the additional catalog describes its YAML source in [00_Index/README.md](01_Resources/00_Index/README.md).

`llms-full.txt` is a derived navigation and annotation bundle. Original catalog records and course documents remain the source of truth.

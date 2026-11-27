# Electricity Measurement Pilot

The [HTML page](index.html) presents one course case through prediction, arithmetic, four explanation views, argument assessment, and transfer. Its [Markdown companion](LESSON.md) preserves all substantive material for reading and LLM use. The broader wiki remains undeveloped; this directory is a local static pilot, not a deployment record.

## Reproduce and Preview

From the repository root:

```sh
python3 03_Data_and_Code/Learning_Design/bill_identity.py
python3 08_Wiki/pilot/build_pilot.py
node 08_Wiki/pilot/test_pilot.cjs
python3 -m http.server 8765 --bind 127.0.0.1
```

Open `http://127.0.0.1:8765/08_Wiki/pilot/`. The HTML also uses relative local assets and needs no model service, account, package installation, tracking script, or application server. Tabs, calculations, and feedback run in the browser. The input response remains in memory and clears on reload. Ordinary hosting infrastructure can have its own access logs.

The page retains links to the surrounding repository. A future deployment must include those destinations or map them to their published equivalents. Copying only this directory would omit the shared figure, inputs, code, and Markdown sources. GitHub synchronization publishes source files; GitHub Pages deployment has not been enabled by this work.

## Editing

Edit `index.html`, `styles.css`, `logic.js`, and `lesson.js`; preserve `LESSON.md` alongside them. `build_pilot.py` refreshes the full Python listing and `reference_data.js` from the standalone program and existing synthetic table. Keep the figure editable in TikZ. Check modified browser inputs independently and inspect keyboard operation and a narrow viewport. [Verification](../../03_Data_and_Code/Learning_Design/VERIFICATION.md) records the checks that ran.

The page uses Illinois colors and the course's parchment direction. No raster illustration, external font, or third-party implementation was copied. The analytical diagram has an equivalent text description.

## Action Under Uncertainty

The `uncertainty` section and matching Markdown text add a static, accessible comparison of error costs, an editable TikZ figure, and questions about records, protection, and remedy. The original bill inputs and feedback remain interactive. The new section links to the full standard-library calculation and optional practice; it collects no responses.

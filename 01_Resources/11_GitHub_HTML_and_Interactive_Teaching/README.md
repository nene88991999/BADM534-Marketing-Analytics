# GitHub, HTML, and Interactive Teaching

Updated October 23, 2026. 10 curated resources. [Master Guide](../README.md).

These are design and hosting references for the later wiki phase. GitHub Pages serves static files. Browser Python and external notebooks offer different ways to add executable exercises; their package support and resource limits need testing.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| W01 | [What Is GitHub Pages?](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) | Instructor | Guide |
| W02 | [Quarto: Creating a Website](https://quarto.org/docs/websites/) | Instructor | Guide |
| W03 | [Quarto: GitHub Pages](https://quarto.org/docs/publishing/github-pages.html) | Instructor | Guide |
| W04 | [Jupyter Book Documentation](https://jupyterbook.org/) | Instructor | Guide |
| W05 | [JupyterLite Documentation](https://jupyterlite.readthedocs.io/en/stable/) | Instructor | Guide |
| W06 | [marimo: WebAssembly HTML Export](https://docs.marimo.io/guides/exporting/webassembly_html/) | Instructor | Guide |
| W07 | [Pyodide: Using Pyodide](https://pyodide.org/en/stable/usage/index.html) | Instructor | Guide |
| W08 | [MDN: Learn Web Development](https://developer.mozilla.org/en-US/docs/Learn_web_development) | Reference | Guide |
| W09 | [W3C Web Accessibility Tutorials](https://www.w3.org/WAI/tutorials/) | Instructor | Guide |
| W10 | [Google Colab FAQ](https://research.google.com/colaboratory/faq.html) | Instructor | Guide |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### W01. What Is GitHub Pages?

**Source:** GitHub. [Open Resource](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages). **Priority:** Instructor. **Syllabus:** Cross-course.

Hosting a static website from repository content.

**Teaching Use:** Establish the hosting constraints before selecting a wiki implementation.

**Conditions and Adaptation:** A static host does not provide a persistent Python server or a safe place for secret API keys.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W02. Quarto: Creating a Website

**Source:** Posit and Quarto contributors. [Open Resource](https://quarto.org/docs/websites/). **Priority:** Instructor. **Syllabus:** Cross-course.

Navigation, HTML publishing, code, and integrated documents.

**Teaching Use:** Evaluate as a maintainable source-to-HTML authoring system.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W03. Quarto: GitHub Pages

**Source:** Posit and Quarto contributors. [Open Resource](https://quarto.org/docs/publishing/github-pages.html). **Priority:** Instructor. **Syllabus:** Cross-course.

Local rendering and automated publishing to GitHub Pages.

**Teaching Use:** Compare a simple rendered docs folder with an automated publishing workflow.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W04. Jupyter Book Documentation

**Source:** Jupyter Book contributors. [Open Resource](https://jupyterbook.org/). **Priority:** Instructor. **Syllabus:** Cross-course.

An authoring approach for computational books and course materials.

**Teaching Use:** Compare chapter navigation, references, and notebook integration with Quarto.

**Conditions and Adaptation:** Use documentation for the selected current major version; avoid mixing older and newer build systems.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W05. JupyterLite Documentation

**Source:** Project Jupyter. [Open Resource](https://jupyterlite.readthedocs.io/en/stable/). **Priority:** Instructor. **Syllabus:** Cross-course.

Browser-hosted notebooks deployable as static files.

**Teaching Use:** Assess a lightweight browser coding sandbox for Python fundamentals.

**Conditions and Adaptation:** Package compatibility, browser storage, and memory need testing with course examples.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W06. marimo: WebAssembly HTML Export

**Source:** marimo contributors. [Open Resource](https://docs.marimo.io/guides/exporting/webassembly_html/). **Priority:** Instructor. **Syllabus:** Cross-course.

Exporting reactive Python notebooks for browser execution.

**Teaching Use:** Evaluate a compact parameter-changing activity that can run on a static host.

**Conditions and Adaptation:** WebAssembly package support and external asset downloads constrain deployment.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W07. Pyodide: Using Pyodide

**Source:** Pyodide contributors. [Open Resource](https://pyodide.org/en/stable/usage/index.html). **Priority:** Instructor. **Syllabus:** Cross-course.

Running Python in a web browser through WebAssembly.

**Teaching Use:** Investigate whether the small numerical core of a lesson can run entirely in the browser.

**Conditions and Adaptation:** Many native or heavy libraries require alternatives or external execution.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W08. MDN: Learn Web Development

**Source:** MDN contributors. [Open Resource](https://developer.mozilla.org/en-US/docs/Learn_web_development). **Priority:** Reference. **Syllabus:** Cross-course.

HTML, CSS, JavaScript, and accessible web fundamentals.

**Teaching Use:** Keep as a reference for custom wiki components and reading generated front-end code.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W09. W3C Web Accessibility Tutorials

**Source:** W3C Web Accessibility Initiative. [Open Resource](https://www.w3.org/WAI/tutorials/). **Priority:** Instructor. **Syllabus:** Cross-course.

Accessible page structure, images, tables, forms, and controls.

**Teaching Use:** Set keyboard access, clear labels, readable tables, and text alternatives as design requirements.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### W10. Google Colab FAQ

**Source:** Google Research. [Open Resource](https://research.google.com/colaboratory/faq.html). **Priority:** Instructor. **Syllabus:** Cross-course.

Hosted notebook execution and service constraints.

**Teaching Use:** Evaluate a launch-in-Colab option for exercises that exceed browser package support.

**Conditions and Adaptation:** Requires external service access; quotas and availability can change.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

## Later Wiki Decisions

- [Hosting and Interactivity Notes](Design_Notes/README.md)

# Hosting and Interactivity Notes

[Technical Sources](../README.md) | [Resource Library](../../README.md)

The resource collection supports a course site built around short explanations, worked examples, executable exercises, and feedback. These notes identify design questions for the next phase. No website, repository, or deployment has been created.

## Hosting Constraint

[GitHub Pages](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages) hosts static HTML, CSS, and JavaScript. Python can execute during a build, inside a compatible browser runtime, or through an external notebook service. A public static page cannot safely contain a secret API key or supply a persistent server-side Python session.

## Options to Compare

| Approach | Potential Role | What to Check Before Selection |
| --- | --- | --- |
| [Quarto](https://quarto.org/docs/websites/) with [GitHub Pages](https://quarto.org/docs/publishing/github-pages.html) | Written course chapters, navigation, references, code, rendered outputs, and embedded visualizations | Authoring convenience, search, navigation, build reproducibility, and integration of selected interactive exercises |
| [Jupyter Book](https://jupyterbook.org/) | Notebook-centered course chapters and computational references | Current major-version workflow, migration implications, and how execution is supplied |
| Plain HTML/CSS/JavaScript with [MDN references](https://developer.mozilla.org/en-US/docs/Learn_web_development) | Small custom activities with direct control over behavior and presentation | Maintenance burden, consistency across modules, and accessibility |
| [JupyterLite](https://jupyterlite.readthedocs.io/en/stable/) or [Pyodide](https://pyodide.org/en/stable/usage/index.html) | Lightweight Python exercises that run on a static site | Exact package compatibility, memory, loading time, file handling, and persistence |
| [marimo WebAssembly export](https://docs.marimo.io/guides/exporting/webassembly_html/) | Reactive exercises where controls update calculations and visualizations | Browser-compatible packages, externally loaded assets, and notebook size |
| [Colab](https://research.google.com/colaboratory/faq.html) launch links | Heavier Python exercises and a familiar hosted notebook environment | Student accounts, runtime limits, data loading, and reproducible saved outputs |

A promising prototype to evaluate is a Quarto course site with small client-side interactions and external notebook launch links for heavier analysis. That recommendation is an initial inference from the documentation and the mix of collected resources. It should be tested against Jupyter Book and a small browser-Python example before becoming the final design.

## Representative Prototype Checks

A single future module can test the main requirements: readable explanation; a small customer dataset; an interactive chart; a parameter-changing example; an editable code exercise; a self-check with feedback; and a link to a full notebook. Use the [W3C tutorials](https://www.w3.org/WAI/tutorials/) to check keyboard access, meaningful labels, readable tables, and text alternatives.

Test the prototype on a fresh browser and a student-like account. Confirm package support with the actual intended exercise. Small pandas and statistical examples are more plausible browser candidates than Bayesian sampling, deep-learning stacks, or large review datasets. Retain downloadable notebooks and static explanatory outputs when execution depends on an external service.

Keep instructor-only answer keys, private course information, and restricted PDFs outside the public site. The source catalog is suitable for a reading directory after reviewing which fields and links should be public. The present instructor library is intentionally broader than the final student-facing site.

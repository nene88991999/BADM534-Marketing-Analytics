# Wiki Design Patterns From PyStatlas

[PyStatlas](https://warint.github.io/pystatlas/) provides a useful architecture for a GitHub-hosted course reference: static HTML, searchable example cards, family filters, and detail pages containing the interpretation, image, source code, libraries, and data attribution. Its metadata live in Python docstrings and YAML, and a builder produces the public pages. The code copy and download controls are visible on the calibration detail page; only search and navigation were exercised in this review.

## A Course Page

Start with the managerial question, the data available at the decision date, and the comparison needed to answer it. Follow with the chart and a short interpretation. Place the complete program, input data dictionary, aggregate table, environment, and run command beside the result. Include stable links to the module notes, relevant slides, original sources, and corresponding Markdown page.

The chart should remain understandable without its image: state the units, denominator, population, directions of comparison, key values, and uncertainty meaning in text. An LLM should be able to retrieve that explanation without running a browser or inferring data from pixels.

## Navigation and Publication

| Pattern | Course Implementation |
| --- | --- |
| Searchable cards | Search managerial questions, methods, module IDs, and dataset names. |
| Statistical family filters | Add module and decision filters, such as retention, product design, pricing, and forecasting. |
| Detail page with code | Offer a complete downloadable Python file and small inputs with relative paths. |
| Shared metadata | Generate HTML navigation and Markdown indexes from the same reviewed records. |
| Static hosting | Use GitHub Pages with a client-side search index and stable relative links. |
| Source transparency | Include provenance, dataset rights, version, and exact execution status in supporting documentation. |

Keep `AGENTS.md`, `course.json`, `llms.txt`, and the Markdown companions accessible from the index. Give released requirements precedence over readings and examples. Preserve the distinction between reference code, adapted code, and an executed course example. During rendering, surface analytical warnings and verify plotted values against output tables.

This document records design choices for the future course wiki. It does not introduce a new site or alter publication permissions.

# Python, Data, and Reproducibility

Updated October 23, 2026. 10 curated resources. [Master Guide](../README.md).

Begin with tables, functions, notebook execution, and elementary checks. Students need enough Python literacy to inspect data and explain generated code. Use the author notebooks as adaptation sources.

## Reading Guide

| ID | Resource | Priority | Format |
| --- | --- | --- | --- |
| P01 | [The Python Tutorial](https://docs.python.org/3/tutorial/) | Core | Guide |
| P02 | [Python for Data Analysis, Third Edition](https://wesmckinney.com/book/) | Core | Open web book |
| P03 | [Getting Started Tutorials: pandas](https://pandas.pydata.org/docs/getting_started/intro_tutorials/) | Core | Guide |
| P04 | [NumPy: The Absolute Basics for Beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) | Reference | Guide |
| P05 | [Plotting and Programming in Python](https://swcarpentry.github.io/python-novice-gapminder/) | Core | Text lessons |
| P06 | [JupyterLab User Guide](https://jupyterlab.readthedocs.io/en/stable/user/) | Reference | Guide |
| P07 | [uv: Working on Projects](https://docs.astral.sh/uv/guides/projects/) | Reference | Guide |
| P08 | [Version Control with Git](https://swcarpentry.github.io/git-novice/) | Core | Text lessons |
| P09 | [pytest: Get Started](https://docs.pytest.org/en/stable/getting-started.html) | Core | Guide |
| P10 | [Python for Marketing Research and Analytics: Author Repository](https://github.com/python-marketing-research/python-marketing-research-1ed) | Core | Code and data repository |

Core identifies candidates for the eventual required readings. Reference material supports exercises and troubleshooting. Optional material supports extensions. Instructor material informs teaching and assessment; these labels are recommendations, not a finalized syllabus.

## Annotated Resources

### P01. The Python Tutorial

**Source:** Python Software Foundation. [Open Resource](https://docs.python.org/3/tutorial/). **Priority:** Core. **Syllabus:** M1.

Language basics, control flow, functions, data structures, and exceptions.

**Teaching Use:** Assign selected sections as a reference while students explain a generated data-cleaning function.

**Conditions and Adaptation:** The tutorial assumes some general programming familiarity.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P02. Python for Data Analysis, Third Edition

**Source:** Wes McKinney. [Open Resource](https://wesmckinney.com/book/). **Priority:** Core. **Syllabus:** M1.

NumPy, pandas, cleaning, aggregation, joins, and time series.

**Teaching Use:** Use chapters 5, 7, 8, and 10 as the reference for customer-data preparation.

**Conditions and Adaptation:** The web book explicitly restricts copying; link to chapters. Code has separate MIT terms.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Web book: no copying or reproduction; companion code is MIT-licensed.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P03. Getting Started Tutorials: pandas

**Source:** pandas contributors. [Open Resource](https://pandas.pydata.org/docs/getting_started/intro_tutorials/). **Priority:** Core. **Syllabus:** M1.

Reading tables, selecting rows, grouping, reshaping, and combining data.

**Teaching Use:** Ask AI to implement a customer-level aggregation, then check counts and totals against a hand calculation.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P04. NumPy: The Absolute Basics for Beginners

**Source:** NumPy contributors. [Open Resource](https://numpy.org/doc/stable/user/absolute_beginners.html). **Priority:** Reference. **Syllabus:** M1.

Arrays, dimensions, indexing, and vectorized calculation.

**Teaching Use:** Trace array shapes in a simple simulation and check a vectorized result against a loop.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P05. Plotting and Programming in Python

**Source:** Software Carpentry. [Open Resource](https://swcarpentry.github.io/python-novice-gapminder/). **Priority:** Core. **Syllabus:** M1.

A structured introductory Python sequence with exercises.

**Teaching Use:** Borrow the lesson progression and use it to design a short prerequisite refresher.

**Conditions and Adaptation:** Examples use Gapminder rather than marketing data.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P06. JupyterLab User Guide

**Source:** Project Jupyter. [Open Resource](https://jupyterlab.readthedocs.io/en/stable/user/). **Priority:** Reference. **Syllabus:** M1.

Notebook editing, kernels, files, and the execution environment.

**Teaching Use:** Teach restart-and-run-all as a check that a submitted notebook reproduces its outputs.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P07. uv: Working on Projects

**Source:** Astral. [Open Resource](https://docs.astral.sh/uv/guides/projects/). **Priority:** Reference. **Syllabus:** M1.

Project environments, dependencies, and lockfiles.

**Teaching Use:** Pin a small analysis environment for local AI coding and retain its lockfile.

**Conditions and Adaptation:** Keep a browser notebook option for students who cannot install local tools.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P08. Version Control with Git

**Source:** Software Carpentry. [Open Resource](https://swcarpentry.github.io/git-novice/). **Priority:** Core. **Syllabus:** M1.

Commits, history, collaboration, and resolving conflicts.

**Teaching Use:** Compare an AI-generated change with the preceding commit and explain what changed.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P09. pytest: Get Started

**Source:** pytest contributors. [Open Resource](https://docs.pytest.org/en/stable/getting-started.html). **Priority:** Core. **Syllabus:** M1.

Small automated checks and readable test failures.

**Teaching Use:** Write checks for row counts, duplicate customers, impossible prices, and known examples before accepting generated code.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Link to the source; redistribution rights not established.

**Local Files:** Annotated link and Finder bookmark only; no full-text or dataset copy saved.

**Verification:** Source URL retrieved successfully on October 23, 2026.

### P10. Python for Marketing Research and Analytics: Author Repository

**Source:** Jason Schwarz, Chris Chapman, and Elea McDonnell Feit. [Open Resource](https://github.com/python-marketing-research/python-marketing-research-1ed). **Priority:** Core. **Syllabus:** M1-M4; M7.

Book companion notebooks, data, and functions for marketing analysis.

**Teaching Use:** Select short portions of the regression, clustering, and classification notebooks for adaptation.

**Conditions and Adaptation:** Published companion code may need dependency updates. Book text is separate from repository materials. Downloaded examples use shortened data URLs, Colab helpers, generated files, and companion functions. Local raw data and functions are preserved; adaptation and rerunning are still required.

**Access and Reuse:** Public web resource; linked services may require an account or payment. Downloaded repository LICENSE: Apache-2.0. Retain attribution and notices; check separate dataset and third-party content terms.

**Local Files:**

- [Source_Notebooks/Marketing_Research/Data/chapter2_data.csv](Source_Notebooks/Marketing_Research/Data/chapter2_data.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter3_data.csv](Source_Notebooks/Marketing_Research/Data/chapter3_data.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter4_data.csv](Source_Notebooks/Marketing_Research/Data/chapter4_data.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter5_data.csv](Source_Notebooks/Marketing_Research/Data/chapter5_data.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter7_data.csv](Source_Notebooks/Marketing_Research/Data/chapter7_data.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter8_data_pt1.csv](Source_Notebooks/Marketing_Research/Data/chapter8_data_pt1.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter8_data_pt2.csv](Source_Notebooks/Marketing_Research/Data/chapter8_data_pt2.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter8_data_pt3.csv](Source_Notebooks/Marketing_Research/Data/chapter8_data_pt3.csv)
- [Source_Notebooks/Marketing_Research/Data/chapter9_data.csv](Source_Notebooks/Marketing_Research/Data/chapter9_data.csv)
- [Source_Notebooks/Marketing_Research/LICENSE](Source_Notebooks/Marketing_Research/LICENSE)
- [Source_Notebooks/Marketing_Research/README.md](Source_Notebooks/Marketing_Research/README.md)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_02_An_overview_of_Python.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_02_An_overview_of_Python.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_03_Describing_Data.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_03_Describing_Data.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_04_Relationships_Between_Continuous_Variables.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_04_Relationships_Between_Continuous_Variables.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_05_Comparing_Groups_Tables_and_Visualizations.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_05_Comparing_Groups_Tables_and_Visualizations.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_06_Comparing_Groups_Statistical_Tests.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_06_Comparing_Groups_Statistical_Tests.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_07_Identifying_Drivers_of_Outcomes_Linear_Models.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_07_Identifying_Drivers_of_Outcomes_Linear_Models.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_08_Additional_Linear_Modeling_Topics.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_08_Additional_Linear_Modeling_Topics.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_09_Reducing_Data_Complexity.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_09_Reducing_Data_Complexity.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_10_Clustering.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_10_Clustering.ipynb)
- [Source_Notebooks/Marketing_Research/notebooks/Chapter_11_Classification.ipynb](Source_Notebooks/Marketing_Research/notebooks/Chapter_11_Classification.ipynb)
- [Source_Notebooks/Marketing_Research/requirements.txt](Source_Notebooks/Marketing_Research/requirements.txt)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/__init__.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/__init__.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter10.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter10.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter11.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter11.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter2.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter2.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter3.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter3.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter6.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter6.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter7.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter7.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter8.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter8.py)
- [Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter9.py](Source_Notebooks/Marketing_Research/python_marketing_research_functions/chapter9.py)

**Verification:** Source URL retrieved successfully on October 23, 2026.

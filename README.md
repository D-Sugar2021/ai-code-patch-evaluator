# ai-code-patch-evaluator
Automated Python static analysis engine using AST to evaluate AI code patches, perform security audits, and check PEP 8 compliance.
# AI Code Patch Evaluator & GitHub Issue Reviewer

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A lightweight, automated Python static analysis framework designed to evaluate AI-generated code patches, audit pull requests, and investigate GitHub code issues before merging.

## 🚀 Features
- **AST Static Analysis:** Parses Python scripts into Abstract Syntax Trees to inspect code structure, functions, classes, and logic.
- **Security Audit:** Automatically flags risky built-in functions (e.g., `eval()`, `exec()`) and wildcard imports (`from module import *`).
- **Code Quality Checks:** Verifies docstring coverage, function complexity, and naming conventions.
- **Automated Report Generation:** Outputs a structured code review report with pass/fail recommendations.

## 📂 Project Structure
```text
ai-code-patch-evaluator/
│
├── patch_evaluator.py      # Core static analysis and evaluation engine
├── sample_target.py        # Sample code patch used for testing
└── README.md               # Documentation


python patch_evaluator.py sample_target.py

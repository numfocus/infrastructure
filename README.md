# NumFOCUS Infrastructure Committee

This repository contains information regarding the NumFOCUS infrastructure.

Main sections:

- [Review Process](https://numfocus.github.io/infrastructure/review_process.html): Information regarding the process for projects to ask for infrastructure requests and what to expect from the review process
- [CI/CD Guide](https://numfocus.github.io/infrastructure/ci_cd_guide/index.html): Information regarding getting CI/CD paid for with NumFOCUS funds.
- [Projects](https://numfocus.github.io/infrastructure/projects/index.html): Information regarding NumFOCUS projects that use shared infrastructure
- [Vendors](https://numfocus.github.io/infrastructure/vendors/index.html): Information about NumFOCUS infrastructure providers (e.g., hosting companies)

## Contact

[To contact the committee, you can use the email address: infrastructure@numfocus.org](infrastructure@numfocus.org)

## Local Setup

This document explains how to set up the infrastructure docs locally.

### Requirements

- Python 3.10+
- pip
- virtualenv (optional)

### Installation

```bash
pip install -r requirements.txt
```

Navigate to the docs directory and Build the documentation locally:

```bash
cd docs
make html
```

```bash
sphinx-build -b html . _build/html
```
To run the documentation server:

```bash
cd _build/html
python -m http.server 8000
```

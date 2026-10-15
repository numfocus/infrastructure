# NumFOCUS Infrastructure Committee

This repository contains information regarding the NumFOCUS infrastructure.

Main sections:

- [Review Process](https://numfocus.github.io/infrastructure/review_process.html): Information regarding the process for projects to ask for infrastructure requests and what to expect from the review process
- [CI/CD Guide](https://numfocus.github.io/infrastructure/ci_cd_guide/index.html): Information regarding getting CI/CD paid for with NumFOCUS funds.
- [Projects](https://numfocus.github.io/infrastructure/projects/index.html): Information regarding NumFOCUS projects that use shared infrastructure
- [Vendors](https://numfocus.github.io/infrastructure/vendors/index.html): Information about NumFOCUS infrastructure providers (e.g., hosting companies)

## Building locally

Use Python 3.15 and create a virtual environment before installing the documentation dependencies:

```bash
python3.15 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd docs
make html
```

Or you can use tox:

```bash
python -m pip install -r requirements-dev.txt
tox -e build_docs
```

## Publishing

The Test and Deploy workflow builds the documentation and publishes it with GitHub's native Pages Actions after the style and documentation checks pass on `main`.
Pull requests build the documentation without deploying it.

## Contact

[To contact the committee, you can use the email address: infrastructure@numfocus.org](mailto:infrastructure@numfocus.org)

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

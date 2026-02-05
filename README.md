# NumFOCUS Infrastructure Committee

This repository contains information regarding the NumFOCUS infrastructure.

Main sections:

- [Review Process](https://numfocus.github.io/infrastructure/review_process.html): Information regarding the process for projects to ask for infrastructure requests and what to expect from the review process
- [CI/CD Guide](https://numfocus.github.io/infrastructure/ci_cd_guide/index.html): Information regarding getting CI/CD paid for with NumFOCUS funds.
- [Projects](https://numfocus.github.io/infrastructure/projects/index.html): Information regarding NumFOCUS projects that use shared infrastructure
- [Vendors](https://numfocus.github.io/infrastructure/vendors/index.html): Information about NumFOCUS infrastructure providers (e.g., hosting companies)

## Building locally

You can create your own Python virtual environment and do the following:

```bash
pip install -r requirements.txt
cd docs
make html
sphinx-build -b html . _build/html
```

Or you can use tox:

```bash
pip install tox
tox -e build_docs
```

## Contributing

Please see our [Contributing Guidelines](CONTRIBUTING.md) for information on how to contribute to this project.

## Contact

[To contact the committee, you can use the email address: infrastructure@numfocus.org](infrastructure@numfocus.org)

## License

This project is licensed under the MIT License.
See the [LICENSE](LICENSE) file for details.

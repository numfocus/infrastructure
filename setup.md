# Setup Guide

This document explains how to set up the infrastructure docs locally.

## Requirements

- Python 3.10+
- pip
- virtualenv (optional)

## Installation

```bash
pip install -r requirements.txt

```
Navigate to the docs directory and Build the documentation locally:

```bash
cd docs
make html
```

To run the documentation server:

```bash
sphinx-autobuild . _build/html
```
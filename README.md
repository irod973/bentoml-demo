# bentoml-demo

[![check.yml](https://github.com/irod973/bentoml-demo/actions/workflows/check.yml/badge.svg)](https://github.com/irod973/bentoml-demo/actions/workflows/check.yml)
[![publish.yml](https://github.com/irod973/bentoml-demo/actions/workflows/publish.yml/badge.svg)](https://github.com/irod973/bentoml-demo/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://irod973.github.io/bentoml-demo/)
[![License](https://img.shields.io/github/license/irod973/bentoml-demo)](https://github.com/irod973/bentoml-demo/blob/main/LICENCE.txt)
[![Release](https://img.shields.io/github/v/release/irod973/bentoml-demo)](https://github.com/irod973/bentoml-demo/releases)

# Description	

Exploring BentoML for model serving and inference. Adapted from https://github.com/musikalkemist/mldeployment/tree/main

# Installation

Initialize your project with the provided `just` command.
```bash	
# Install dependencies and pre-commit hooks	
uv run just install	
```
# Usage

Test the example package
```bash
uv run bentoml-demo
```

Test the example API with Docker:
```bash	
uv add fastapi uvicorn	
uv run just package	

# Invoke docker compose	
uv run just docker-compose

# Or run with docker compose	
docker compose up --build	

# Or run with docker	
# Note: specify platform if running on Apple M chip 	
docker build --platform linux/amd64 -t bentoml-demo-image -f Dockerfile .	
docker run -it --platform linux/amd64 --name bentoml-demo-ctr -p 8000:8000 bentoml-demo-image	
```

Test the API using the local environment:
```bash
cd src	
uv run uvicorn example_app.main:app --reload
```

## Development Features

(This section was copied into the created project's README so tool info is available to users.)

* **Streamlined Project Structure:** A well-defined directory layout for source code, tests, documentation, tasks, and Docker configurations.
Uv Integration: Effortless dependency management and packaging with [uv](https://docs.astral.sh/uv/).
* **Automated Testing and Checks:** Pre-configured workflows using [Pytest](https://docs.pytest.org/), [Ruff](https://docs.astral.sh/ruff/), [Mypy](https://mypy.readthedocs.io/), [Bandit](https://bandit.readthedocs.io/), and [Coverage](https://coverage.readthedocs.io/) to ensure code quality, style, security, and type safety.
* **Pre-commit Hooks:** Automatic code formatting and linting with [Ruff](https://docs.astral.sh/ruff/) and other pre-commit hooks to maintain consistency.
* **Dockerized Deployment:** Dockerfile and docker-compose.yml for building and running the package within a containerized environment ([Docker](https://www.docker.com/)).
* **uv+just Task Automation:** [just](https://github.com/casey/just) commands to simplify development workflows such as cleaning, installing, formatting, checking, building, documenting and running the project.
* **Comprehensive Documentation:** [pdoc](https://pdoc.dev/) generates API documentation, and Markdown files provide clear usage instructions.
* **GitHub Workflow Integration:** Continuous integration and deployment workflows are set up using [GitHub Actions](https://github.com/features/actions), automating testing, checks, and publishing.


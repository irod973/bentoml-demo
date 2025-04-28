# bentoml-demo

[![check.yml](https://github.com/irod973/bentoml-demo/actions/workflows/check.yml/badge.svg)](https://github.com/irod973/bentoml-demo/actions/workflows/check.yml)
[![publish.yml](https://github.com/irod973/bentoml-demo/actions/workflows/publish.yml/badge.svg)](https://github.com/irod973/bentoml-demo/actions/workflows/publish.yml)
[![Documentation](https://img.shields.io/badge/documentation-available-brightgreen.svg)](https://irod973.github.io/bentoml-demo/)
[![License](https://img.shields.io/github/license/irod973/bentoml-demo)](https://github.com/irod973/bentoml-demo/blob/main/LICENCE.txt)
[![Release](https://img.shields.io/github/v/release/irod973/bentoml-demo)](https://github.com/irod973/bentoml-demo/releases)

# Description	

Exploring BentoML for model serving and inference. Adapted from https://github.com/musikalkemist/mldeployment/tree/main. Note that the example originally used the v1.0.0 library and there were various deprecation warnings

# Installation

Initialize your project with the provided `just` command.
```bash	
# Install dependencies and pre-commit hooks	
uv run just install	
```
# Usage

## Train model and save to BentoML model store

This includes a script to train a CNN digit classifier using the MNIST dataset
```bash
cd src/
uv run python bentoml_demo/training.py 
uv run python bentoml_demo/savemodeltobento.py
```

#### Deprecation warning

```
(bentoml-demo) ➜  bentoml_demo git:(main) ✗ uv run python savemodeltobento.py
/Users/irvingrodriguez/Documents/workspace/bentoml-demo/src/bentoml_demo/savemodeltobento.py:13: BentoMLDeprecationWarning: `bentoml.keras` is deprecated since v1.4 and will be removed in a future version.
```

## Build the model + service into a bento

This is defined in `bentoml_demo/service/bentofile.yaml`.

This will output a tag that can be used  e.g. `Bento(tag="mnist_classifier:q333ynrengyagmpy").`
```bash
cd src/bentoml_demo/service
bentoml build
```

## Serve model through a bento

```
bentoml serve mnist_classifier:latest --production
```

#### Deprecation warning

```
DeprecationWarning: The parameter '--production' is 
deprecated and will be removed in the future. 
(Current behaviour: This is enabled by default. To 
run in development mode, use '--development'.)
```

## Containerize a bento

This allows you to port your app to other environments e.g. k8s
```
bentoml containerize mnist_classifier:latest
```

You can then try running a container (todo: add the `bentoml containerize` to the `containers` task)

## Deployment options

Kubernetes via (Yatai)[https://github.com/bentoml/Yatai]

## Create a stand-alone BentoML service

This utilizes (BentoML runners)[https://docs.bentoml.com/en/1.1/concepts/runner.html]. This is very similar to a FastAPI endpoint but includes some optimizations like adaptive batching.
```bash
cd src/bentoml_demo
bentoml serve service.service:mnist_service --reload
```

#### Deprecation warning

```
/Users/irvingrodriguez/Documents/workspace/bentoml-demo/.venv/lib/python3.12/site-packages/bentoml/_internal/models/model.py:354: BentoMLDeprecationWarning: `Runner` is deprecated since BentoML v1.4 and will be removed in a future version. Please upgrade to new style services.
  return Runner(
/Users/irvingrodriguez/Documents/workspace/bentoml-demo/src/bentoml_demo/service/service.py:14: BentoMLDeprecationWarning: `bentoml.Service` is deprecated since BentoML v1.4 and will be removed in a future version. Please upgrade to @bentoml.service().
  mnist_service = bentoml.Service("mnist_classifier", runners=[classifier_runner])
```

## bentoml cli

Some useful cli commands. General info:
```bash
bentoml -h
```

```bash
bentoml models {list, get, delete, push, pull}
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


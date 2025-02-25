# Political NER and Sentiment Analysis

## Prerequisites

- Have python installed or use pipx
- Install poetry (ref - https://python-poetry.org/docs/ )

- clone the repository 

## Versioning and dependency 

- packages can be added by "poetry add <package>"
- install packages based on configs in pyproject.toml "poetry install"

## Activate Dev Environment

To optimize the dev enviroment can be done on Jupyter notebook with vscode. 

Enabling environment on terminal "poetry env activate"
- but this command only prints another script to activate a virtual environment in your current shell
- to use copy the output and paste and run in terminal

## Using with Jupyter Notebook in Vscode

Ref - https://hippocampus-garden.com/jupyter_poetry_pipenv/

```bash
# this will run a jupyter notebook server inside venv managed by poetry
poetry run jupyter notebook
```
#!/usr/bin/env sh

set -x -e

poetry run black .

poetry run mypy --namespace-packages -p charmonium.async_subprocess

poetry run python3 -m pytest

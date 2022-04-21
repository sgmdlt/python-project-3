repl:
	poetry run ipython

install:
	poetry install

run:
	poetry run page-loader

build: check
	rm -rf dist/
	poetry build

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml

lint:
	poetry run flake8 page_loader/

selfcheck:
	poetry check

check: selfcheck test lint

package-install:
	python3 -m pip uninstall hexlet-code -y
	python3 -m pip install --user dist/*.whl

.PHONY: install test lint selfcheck check build
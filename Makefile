# Makefile for Project Chimera

.PHONY: setup test spec-check

setup:
	pip install --upgrade pip
	if [ -f pyproject.toml ]; then pip install .; elif [ -f requirements.txt ]; then pip install -r requirements.txt; fi

test:
	docker build -t chimera-test .
	docker run --rm chimera-test pytest tests/

spec-check:
	@echo "Spec check not yet implemented. Add your script here."

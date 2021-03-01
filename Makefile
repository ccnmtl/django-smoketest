# VERSION=1.0.0

# CHANGES:
# 1.0.0 - 2021-02-27 - Initial

VE ?= ./ve
SYS_PYTHON ?= python3
PY_SENTINAL ?= $(VE)/sentinal
PIP_VERSION ?= 21.0.1
MAX_COMPLEXITY ?= 9
INTERFACE ?= localhost
RUNSERVER_PORT ?= 8000
PY_DIRS ?= smoketest exceptionstest main testapp
FLAKE8 ?= $(VE)/bin/flake8
PIP ?= $(VE)/bin/pip


all: flake8 test

$(PY_SENTINAL):
	rm -rf $(VE)
	$(SYS_PYTHON) -m venv $(VE)
	$(PIP) install pip==$(PIP_VERSION)
	$(PIP) install .
	$(PIP) install flake8
	touch $@

flake8: $(PY_SENTINAL)
	$(FLAKE8) $(PY_DIRS) --max-complexity=$(MAX_COMPLEXITY)

test: $(PY_SENTINAL)
	./ve/bin/python runtests.py

clean:
	rm -rf $(VE)
	find . -name '*.pyc' -exec rm {} \;

.PHONY: test flake8 clean

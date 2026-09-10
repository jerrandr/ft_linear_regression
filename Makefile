
VENV := .venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip

all: train prediction

install:
	@python3 -m venv $(VENV)
	@$(PIP) install --upgrade pip
	@$(PIP) install -r requierment.txt

train:
	@$(PYTHON) train.py

prediction:
	@$(PYTHON) prediction.py

precision:
	@$(PYTHON) bonus/precision_bonus.py

interface:
	@$(PYTHON) bonus/interface_bonus.py

bonus: interface precision

.PHONY: train prediction bonus install precision interface all

# Makefile for VelouraCore

run:
	uvicorn src.api.main:app --reload

test:
	pytest

lint:
	black src/ tests/

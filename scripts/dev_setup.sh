#!/bin/bash
# dev_setup.sh: Setup and run VelouraCore development environment

python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# Run API server
# uvicorn src.api.main:app --reload

echo "[VelouraCore] Development environment ready. Activate venv and run API with:"
echo "source .venv/bin/activate && uvicorn src.api.main:app --reload"

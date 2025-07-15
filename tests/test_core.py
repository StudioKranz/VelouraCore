import os
import pytest
from config import settings
import subprocess

def test_env_loading():
    assert hasattr(settings, 'OPENAI_API_KEY')
    assert hasattr(settings, 'HUGGINGFACE_TOKEN')

def test_main_runs():
    result = subprocess.run(['python', 'src/main.py'], capture_output=True, text=True)
    assert result.returncode == 0
    assert 'VelouraCore Phase 2: Project Status' in result.stdout

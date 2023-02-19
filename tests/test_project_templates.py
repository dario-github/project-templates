import logging
from pathlib import Path

import pytest


PROJECT_ROOT_DIR = Path(__file__).parent.parent


if __name__ == "__main__":
    pytest.main(["-v", "-s", "-q", "test_project_templates.py"])

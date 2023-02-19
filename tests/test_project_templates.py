import logging
from pathlib import Path

import pytest
from project_templates.template import template_func

PROJECT_ROOT_DIR = Path(__file__).parent.parent


def test_main():
    template_func()


if __name__ == "__main__":
    pytest.main(["-v", "-s", "-q", "test_project_templates.py"])

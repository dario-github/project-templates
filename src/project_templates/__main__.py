import logging
import traceback
from pathlib import Path

import typer
from project_templates.parameter.log import config_log

app = typer.Typer()

PROJECT_ROOT_DIR = Path(__file__).parent.parent.parent


@app.command()
def main():
    """main function, use `python -m project-templates main` to run this."""
    config_log(
        PROJECT_ROOT_DIR.stem,
        "main",
        log_root=(PROJECT_ROOT_DIR / "logs").as_posix(),
        print_terminal=True,
        enable_monitor=False,
    )
    print("Hello World!")


if __name__ == "__main__":
    app()

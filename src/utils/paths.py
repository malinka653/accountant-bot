from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent.parent
DB_DIR = ROOT_DIR / "database"
LOG_DIR = ROOT_DIR / "logs"


def from_root(*paths):
    return ROOT_DIR.joinpath(*paths)

from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent.resolve()
DATA_PATH: Path = ROOT_PATH / "data"
TESTS_PATH: Path = ROOT_PATH / "tests"

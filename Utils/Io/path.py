from pathlib import Path

def safe_open(path) :
    Path(path).mkdir(parents=True, exist_ok=True)
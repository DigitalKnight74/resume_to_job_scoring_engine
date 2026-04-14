"""
File input/output utilities.
"""

from pathlib import Path

def load_text_file(file_path: str) -> str:
    """
    Load a tesxt file and return its content as a string.
    """
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return path.read_text(encoding='utf-8').strip()
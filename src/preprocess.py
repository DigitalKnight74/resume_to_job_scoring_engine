"""
Text preprocessing utilities.
"""

import re

STOP_WORDS = {
    'the', 'and', 'or', 'a', 'an', 'to', 'for', 'of', 'in', 'on', 'with', 'by', 'at',
    'from', 'is', 'are', 'was', 'were', 'be', 'as', 'that', 'this', 'it', ' will', 'can', 'using', 'use'
}

def normalize_text(text: str) -> str:
    """
    Lowercase text and remove extra whitespace/punctuation noise.
    """
    text = text.lower()
    # Remove non-alphanumeric characters except spaces and basic punctuation
    text = re.sub(r"[^a-z0-9\s\-\+]", " ", text)
    # Remove extra whitespace
    text = re.sub(r"\s+", " ", text).strip()
    return text

def tokenize(text: str) -> list[str]:
    """
    Split text into tokens and remove stop words.
    """
    normalized = normalize_text(text)
    tokens = normalized.split()
    return [token for token in tokens if token not in STOP_WORDS]
"""
Text preprocessing utilities.
"""

import re
from src.config import SYNONYMS

STOP_WORDS = {
    "the", "and", "or", "a", "an", "to", "for", "of", "in", "on", "with", "by", "at", "from", "is", "are", "was", "were", "be", "as", "that", "this", "it", "will", "can", "using", "use", "our", "your", "their", "we", "you", "they", "all", "any", "each", "every", "job", "role", "position", "work", "working", "company", "team", "employees", "within", "description", "required", "preferred","experience", "skills", "education", "support", "business", "project", "projects", "where", "have", "regarding", "not", "first", "like", "play", "into"
}

def apply_synonyms(text: str) -> str:
    """
    Replace known synonyms with normalized terms.
    """
    for key, value in SYNONYMS.items():
        text = re.sub(rf"\b{key}\b", value, text)
    return text

def normalize_text(text: str) -> str:
    """
    Lowercase text and remove extra whitespace/punctuation noise.
    """
    text = text.lower()
    text = apply_synonyms(text)
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
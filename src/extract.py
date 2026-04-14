"""
Keyword and skill extraction logic.
"""

from collections import Counter
from src.preprocess import normalize_text, tokenize

def extract_keywords(text: str, min_token_length: int = 3) -> list[str]:
    """
    Extract keywords from text using simple token fitlering.
    """
    tokens = tokenize(text)
    keywords = [token for token in tokens if len(token) >= min_token_length]
    return keywords

def extract_top_keywords(text: str, top_n: int = 25) -> list[tuple[str, int]]:
    """
    Return the most common keywords and their counts.
    """
    
    keywords = extract_keywords(text)
    counts = Counter(keywords)
    return counts.most_common(top_n)

def extract_skills(text: str, skill_taxonomy: dict) -> dict[str, list[str]]:
    """
    Extract mactcing skills from text using hte provided skill taxonomy.
    Returns matched skill grouped by category.
    """
    normalized_text = normalize_text(text)
    matched = {}
    
    for category, skills in skill_taxonomy.items():
        found = []
        for skill in skills:
            if skill.lower() in normalized_text:
                found.append(skill)
        matched[category] = sorted (set(found))
    
    return matched

def flatten_skill_matches(skill_matches: dict[str, list[str]]) -> set[str]:
    """
    Flatten category-ground skill matches into a unique set.
    """

    flat = set()
    for skills in skill_matches.values():
        flat.update(skill.lower() for skill in skills)
    return flat
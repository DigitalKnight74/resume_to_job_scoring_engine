"""
Keyword and skill extraction logic.
"""

from collections import Counter
from src.preprocess import normalize_text, tokenize

LOW_VALUE_TERMS = {
    # Hiring Fluff Words
    "dynamic", "fast-paced", "innovative", "collaborative", "passionate",
    "motivated", "results-driven", "detail-oriented", "proactive", "self-starter",
    "go-getter", "high-performing", "energetic", "agile",

    # Culture/Vibe Fluff
    "ambiguity", "culture", "engaging", "environment", "excellence", "family", 
    "flat", "fun", "hard", "hierarchy", "mentality", "mindset", "organization", 
    "ownership", "people", "startup", "thrive",

    # Responsibility Fog
    "action", "alignment", "collaborate", "cross", "functional", "deliverables",
    "drive", "enable", "ensure", "initiatives", "insights", "leadership", 
    "manage", "outcomes", "own", "partner", "processes", "stakeholder", "stakeholders",
    "strategic", "translate",

    # Performance & Impact Buzzwords
    "create", "data", "deliver", "drive", "efficiency", "enhance", "impact", "improve",
    "leverage", "optimize", "performance", "results", "scale", "solution", "solutions",
    "value",
     
    # Skill Inflation/Resume Traps
    "ability", "equivalent", "exposure", "familiarity", "knowledge", "learn", "nice",
    "qualifications", "quickly",

    # Red Flag Phrases
    "competitive", "deadlines", "environment", "evolving", "ground", "hats", "high",
    "hit", "many", "priorities", "pto", "runnning", "salary", "startup", "tight",
    "unlimited", "visibility", "wear",

    # Data Science Specific
    "alignment", "analysis", "across", "bootcamp", "business", "christian", "clear",
    "club", "competitive", "culture", "customer", "decisions", "executive", "insights",
    "leadership", "performance", "power", "professional",  "project", "projects", 
    "retention", "science", "supporting", "technical", "through", "timelines", 
    "tripleten", "university", "workplace"
}

def extract_keywords(text: str, min_token_length: int = 3) -> list[str]:
    """
    Extract keywords from text using simple token fitlering.
    """
    tokens = tokenize(text)
    keywords = [
        token for token in tokens
        if len(token) >= min_token_length
        and not token.isdigit()
        and token not in LOW_VALUE_TERMS
    ]
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
    Extract mactching skills from text using hte provided skill taxonomy.
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
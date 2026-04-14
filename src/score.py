"""
Scoring logic for resume-to-job matching.
"""

from src.extract import extract_keywords, extract_skills, flatten_skill_matches

def compute_keyword_overlap_score(resume_text: str, jd_text: str) -> float:
    """
    Compute overlap score between resume and job description keywords.
    """
    resume_keywords = set(extract_keywords(resume_text))
    jd_keywords = set(extract_keywords(jd_text))

    if not jd_keywords:
        return 0.0
    
    overlap = resume_keywords.intersection(jd_keywords)
    return round((len(overlap) / len(jd_keywords)) * 100, 2)

def compute_skill_match_score(resume_text: str, jd_text: str, skill_taxonomy:dict) -> tuple[float, set[str], set[str]]:
    """
    Compute skill match score and return matched and missing skills.
    """
    resume_skill_matches = extract_skills(resume_text, skill_taxonomy)
    jd_skill_matches = extract_skills(jd_text, skill_taxonomy)
    
    resume_skills = flatten_skill_matches(resume_skill_matches)
    jd_skills = flatten_skill_matches(jd_skill_matches)
    
    if not jd_skills:
        return 0.0, set(), set()
    
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)
    score = round((len(matched) / len(jd_skills)) * 100, 2)
    
    return score, matched, missing

def compute_skill_category_scores(
    resume_text: str,
    jd_text: str,
    skill_taxonomy: dict
) -> dict[str, float]:
    """
    Compute skill match scores by category.
    """
    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    category_scores = {}

    for category, skills in skill_taxonomy.items():
        jd_skills = {skill.lower() for skill in skills if skill.lower() in jd_lower}
        resume_skills = {skill.lower() for skill in skills if skill.lower() in resume_lower}

        if not jd_skills:
            continue
        
        matched = jd_skills.intersection(resume_skills)
        score = round((len(matched) / len(jd_skills)) * 100, 2)
        category_scores[category] = score
    
    return category_scores

def compute_experience_score(resume_text: str, jd_text: str) -> float:
    """
    Improved experience scoring using flexible phrase matching.
    """

    experience_phrases = [
        'machine learning',
        'data analysis',
        'dashboard',
        'reporting',
        'process improvement',
        'stakeholder communication',
        'feature engineering',
        'model evaluation',
        'workflow automation'
    ]

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    # Only consider phrases relevant to the JD
    relevant_phrases = []

    for phrase in experience_phrases:
        words = phrase.split()
        if any(word in jd_lower for word in words):
            relevant_phrases.append(phrase)
    
    matched_count = 0

    for phrase in relevant_phrases:
        words = phrase.split()

        # Check if ANY meaningful word from teh phrase appears in resume
        if any(word in resume_lower for word in words):
            matched_count += 1
    
    return round((matched_count / len(relevant_phrases)) * 100, 2)

    print("Relevant Phrases:", relevant_phrases)

def compute_education_score(resume_text: str, jd_text: str) -> float:
    """
    Basic education and credential matching.
    """

    education_terms = [
        'bachelor', 'master', 'phd', 'bootcamp', 'certification'
    ]

    resume_lower = resume_text.lower()
    jd_lower = jd_text.lower()

    required_terms = [term for term in education_terms if term in jd_lower]
    if not required_terms:
        return 100.0
    
    matched = [term for term in required_terms if term in resume_lower]
    return round((len(matched) / len(required_terms)) * 100, 2)

def calculate_overall_score(
    keyword_score: float,
    skill_score: float,
    experience_score:float,
    education_score: float,
    scoring_weights: dict
) -> float:
    """
    Calculate weighted overall score.
    """
    overall = (keyword_score * scoring_weights["keyword_score"] +
               skill_score * scoring_weights["skill_score"] +
               experience_score * scoring_weights["experience_score"] +
               education_score * scoring_weights["education_score"]
    )
    return round(overall, 2)
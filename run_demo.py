"""
Simple demo runner for the Resume-to-Job Match Scoring Engine.
"""

from src.config import SKILL_TAXONOMY, SCORING_WEIGHTS
from src.io_utils import load_text_file
from src.score import (
    compute_keyword_overlap_score,
    compute_skill_match_score,
    compute_experience_score,
    compute_education_score,
    calculate_overall_score
)
from src.report import generate_recommendations, build_report

def main() -> None:
    resume_text = load_text_file("data/resumes/resume_george_ds.txt")
    jd_text = load_text_file("data/job_descriptions/jb_data_scientist_01.txt")

    keyword_score = compute_keyword_overlap_score(resume_text, jd_text)
    skill_score, matched_skills, missing_skills = compute_skill_match_score(
        resume_text, jd_text, SKILL_TAXONOMY
    )
    experience_score = compute_experience_score(resume_text, jd_text)
    education_score = compute_education_score(resume_text, jd_text)

    overall_score = calculate_overall_score(
        keyword_score=keyword_score,
        skill_score=skill_score,
        experience_score=experience_score,
        education_score=education_score,
        scoring_weights=SCORING_WEIGHTS
    )

    result = {
        "overall_score": overall_score,
        "keyword_score": keyword_score,
        "skill_score": skill_score,
        "experience_score": experience_score,
        "education_score": education_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": generate_recommendations(missing_skills)
    }

    print(build_report(result))

if __name__ == "__main__":
    main()
"""
Human-readable reporting utilities.
"""

def generate_recommendations(
        missing_skills: set[str],
        keyword_score: float,
        experience_score: float,
        education_score: float
    ) -> list[str]:
    """
    Generate simple recommendations based on missing skills.
    """
    recommendations = []

    if "python" in missing_skills:
        recommendations.append("Add Python project work or technical bullets if applicable.")
    if "sql" in missing_skills:
        recommendations.append("Highlight SQL usage, querying, reporting, or analytical work more explicitly.")
    if "api" in missing_skills:
        recommendations.append("Add API-related work, integrations, or data retrieval examples if you have them.")
    if "machine learning" in missing_skills:
        recommendations.append("Use explicit 'machine learning' language if your experience currently used indirect wording like models or ML.")
    if "certification" in missing_skills:
        recommendations.append("Clarify relevant certifications, training, or bootcamp credentials if they support this role.")
    
    if keyword_score < 30:
        recommendations.append("Align resume language more closely to the job description by mirroring important technical terms and requirement phrasing.")
    if keyword_score < 50:
        recommendations.append("Strengthen experience bullets with clearer technical actions, tools used, and measurable outcomes.")
    if keyword_score < 100:
        recommendations.append("Make education, training, or credential alignment easier to find if the job emphasizes formal qualifications.")

    if not recommendations:
        recommendations.append("Resume appears reasonably aligned. Focus on sharpening impact bullets and measurable outcomes.")
    
    return recommendations

def build_report(result: dict) -> str:
    """
    Build a plain-English summary report.
    """
    lines = [
        "RESUME-TO-JOB MATCH REPORT",
        "-" * 40,
        f"Overall Score: {result['overall_score']}/100",
        f"Keywords Score: {result['keyword_score']}/100",
        f"Skill Score: {result['skill_score']}/100",
        f"Experience Score: {result['experience_score']}/100",
        f"Education Score: {result['education_score']}/100",
        "",
        f"Matched Skills: {', '.join(sorted(result['matched_skills'])) if result['matched_skills'] else 'None'}",
        f"Missing Skills: {', '.join(sorted(result['missing_skills'])) if result['missing_skills'] else 'None'}",
        ""
    ]

    if result.get("category_scores"):
        lines.append("Category Scores:")
        for category, score in result["category_scores"].items():
            lines.append(f"- {category}: {score}/100")
        lines.append("")
    
    lines.append("Recommendatoins:")
    for rec in result ["recommendations"]:
        lines.append(f"- {rec}")
    
    return "\n".join(lines)
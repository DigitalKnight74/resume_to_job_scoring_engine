"""
Human-readable reporting utilities.
"""

def generate_recommendations(missing_skills: set[str]) -> list[str]:
    """
    Generate simple recommendations based on missing skills.
    """
    recommendations = []

    if "python" in missing_skills:
        recommendations.append("Add Python project work or technical bulletsif applicable.")
    if "sql" in missing_skills:
        recommendations.append("Highlight SQL usage, querying, or analytical reporting work.")
    if "airflow" in missing_skills or "aws" in missing_skills:
        recommendations.append("Strengthen cloud or workflow automation language if you have relevant experience.")
    if "dashboard" in missing_skills or "power_bi" in missing_skills:
        recommendations.append("Add dashboarding or BI reporting examples.")
    if not recommendations:
        recommendations.append("Resume appears reasonably aligned. Focus on stronger outcome-based bullets.")
    
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
        "",
        "Recommendations:"
    ]

    for rec in result["recommendations"]:
        lines.append(f"- {rec}")
    
    return "\n".join(lines)
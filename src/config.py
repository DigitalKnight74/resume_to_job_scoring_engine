"""
Configuration settings for the Resume-to-Job Match Scoring Engine.
"""

SKILL_TAXONOMY = {
  "programming_languages": [
    "python", "sql", "r", "javascript", "typescript", "bash"
  ],
  "data_analysis": [
    "pandas", "numpy", "excel", "data cleaning", "data analysis",
    "exploratory data analysis", "eda", "statistics"
  ],
  "machine_learning": [
    "machine learning", "scikit-learn", "xgboost", "classification",
    "regression", "clustering", "feature engineering", "model evaluation", 
    "hyperparameter tuning", "cross-validation"
  ],
  "visualization_bi": [
    "power bi", "tableau", "looker", "looker studio", "matplotlib", 
    "seaborn", "dashboard", "dashboarding", "data visualization"
  ],
  "data_engineering": [
    "etl", "elt", "data pipeline", "pipelines", "workflow automation",
    "airflow", "spark"
  ],
  "databases_cloud": [
    "postgresql", "mysql", "sql server", "snowflake", "aws", "azure", 
    "gcp", "bigquery"
  ],
  "business_operations": [
    "kpi", "reporting", "stakeholder communication", "process improvement",
    "root cause analysis", "cross-functional collaboration", "operations"
  ],
  "project_tools": [
    "git", "github", "jupyter", "notion", "streamlit", "supabase", "api", "rest api"
  ],
  "education_credentials": [
    "bachelor", "master", "bootcamp", "certification", "data science bootcamp"
  ]
}

SCORING_WEIGHTS = {
  "keyword_score": 0.40,
  "skill_score": 0.30,
  "experience_score": 0.20,
  "education_score": 0.10
}
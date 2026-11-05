
from schemas import Resume


SYSTEM_PROMPT = """
You are an expert resume information extraction assistant.

Your task is to extract structured information from unstructured resume text.

Rules:
1. Extract information only from the provided resume.
2. Never invent, assume, or hallucinate information.
3. If a field is missing, return null.
4. If a list field has no information, return an empty list.
5. Preserve the original meaning of the candidate's information.
6. Extract all available work experiences, education records,
   projects, and certifications.
7. Keep dates in their original format when the exact date
   cannot be determined.
8. Categorize skills into the appropriate categories.
9. Return only data matching the provided JSON schema.
10. Do not include explanations outside the JSON.
"""


FEW_SHOT_EXAMPLE = """
Example:

Resume text:
John Smith
Email: john@example.com
Python Developer
Skills: Python, Django, PostgreSQL

Expected JSON:
{
    "personal_info": {
        "full_name": "John Smith",
        "email": "john@example.com",
        "phone": null,
        "location": null,
        "linkedin_url": null,
        "github_url": null,
        "portfolio_url": null
    },
    "professional_summary": "Python Developer",
    "skills": {
        "programming_languages": ["Python"],
        "frameworks": ["Django"],
        "databases": ["PostgreSQL"],
        "tools": [],
        "other_skills": []
    },
    "work_experience": [],
    "education": [],
    "projects": [],
    "certifications": []
}
"""


def build_resume_prompt(resume_text: str) -> str:
    schema = Resume.model_json_schema()

    prompt = f"""
{SYSTEM_PROMPT}

{FEW_SHOT_EXAMPLE}

Required JSON Schema:
{schema}

Now extract information from this resume:

{resume_text}
"""

    return prompt

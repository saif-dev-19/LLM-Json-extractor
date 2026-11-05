
import os

from dotenv import load_dotenv
from google import genai
from google.genai import types

from prompts import build_resume_prompt
from schemas import Resume


load_dotenv()


def extract_resume_data(resume_text: str) -> Resume:
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise ValueError("GEMINI_API_KEY is missing from .env")

    client = genai.Client(api_key=api_key)

    prompt = build_resume_prompt(resume_text)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=Resume,
            temperature=0,
        ),
    )

    if not response.text:
        raise ValueError("Gemini returned an empty response")

    resume = Resume.model_validate_json(response.text)

    return resume


from typing import Literal

from pydantic import BaseModel, Field, HttpUrl


class PersonalInfo(BaseModel):
    full_name: str | None = None
    email: str | None = None
    phone: str | None = None
    location: str | None = None
    linkedin_url: HttpUrl | None = None
    github_url: HttpUrl | None = None
    portfolio_url: HttpUrl | None = None


class Skills(BaseModel):
    programming_languages: list[str] = Field(default_factory=list)
    frameworks: list[str] = Field(default_factory=list)
    databases: list[str] = Field(default_factory=list)
    tools: list[str] = Field(default_factory=list)
    other_skills: list[str] = Field(default_factory=list)


class WorkExperience(BaseModel):
    job_title: str | None = None
    company_name: str | None = None
    location: str | None = None
    employment_type: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    is_current: bool | None = None
    responsibilities: list[str] = Field(default_factory=list)


class Education(BaseModel):
    degree: str | None = None
    institution: str | None = None
    field_of_study: str | None = None
    start_date: str | None = None
    end_date: str | None = None
    grade: str | None = None
    grade_scale: str | None = None
    status: str | None = None


class Project(BaseModel):
    project_name: str | None = None
    description: str | None = None
    technologies: list[str] = Field(default_factory=list)
    project_url: HttpUrl | None = None


class Certification(BaseModel):
    name: str | None = None
    issuing_organization: str | None = None
    issue_date: str | None = None
    credential_url: HttpUrl | None = None


class Resume(BaseModel):
    personal_info: PersonalInfo
    professional_summary: str | None = None
    skills: Skills
    work_experience: list[WorkExperience] = Field(default_factory=list)
    education: list[Education] = Field(default_factory=list)
    projects: list[Project] = Field(default_factory=list)
    certifications: list[Certification] = Field(default_factory=list)


from pathlib import Path

import pymupdf
from docx import Document


def read_resume_file(file_path: str) -> str:
    """
    Extract text from PDF, DOCX, or TXT resume files.
    """

    path = Path(file_path)

    if not path.exists():
        raise FileNotFoundError(f"File not found: {file_path}")

    extension = path.suffix.lower()

    if extension == ".pdf":
        text = extract_pdf_text(path)

    elif extension == ".docx":
        text = extract_docx_text(path)

    elif extension == ".txt":
        text = path.read_text(encoding="utf-8")

    else:
        raise ValueError(
            f"Unsupported file format: {extension}. "
            "Supported formats: PDF, DOCX, TXT"
        )

    text = text.strip()

    if not text:
        raise ValueError(
            "No text found in the resume. "
            "The file may be empty or scanned."
        )

    return text


def extract_pdf_text(path: Path) -> str:
    text_parts = []

    with pymupdf.open(path) as pdf:
        for page in pdf:
            text_parts.append(page.get_text())

    return "\n".join(text_parts)


def extract_docx_text(path: Path) -> str:
    document = Document(path)

    paragraphs = [
        paragraph.text
        for paragraph in document.paragraphs
        if paragraph.text.strip()
    ]

    return "\n".join(paragraphs)

    

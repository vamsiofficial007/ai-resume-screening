import re


def extract_email(text: str) -> str | None:
    """Extract email address from resume text."""

    pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_phone(text: str) -> str | None:
    """Extract Indian phone number from resume text."""

    pattern = r"(?:\+91[\s-]?)?[6-9]\d{9}"

    match = re.search(pattern, text)

    return match.group(0) if match else None


def extract_linkedin(text: str) -> str | None:
    """Extract LinkedIn profile URL from resume text."""

    pattern = r"(?:https?://)?(?:www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

    match = re.search(pattern, text, re.IGNORECASE)

    return match.group(0) if match else None
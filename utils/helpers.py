# Utility helpers placeholder
import re


EMAIL_PATTERN = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

PHONE_PATTERN = r"(?:\+91[\-\s]?)?[6-9]\d{9}"


def extract_email(text):

    match = re.search(EMAIL_PATTERN, text)

    if match:

        return match.group()

    return None


def extract_phone(text):

    match = re.search(PHONE_PATTERN, text)

    if match:

        return match.group()

    return None


def clean_text(text):

    text = re.sub(r"\s+", " ", text)

    return text.strip()
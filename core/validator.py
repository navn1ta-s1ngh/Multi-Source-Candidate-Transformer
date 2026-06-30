import re

from models.partial_candidate import PartialCandidateProfile


class ValidationEngine:
    """Validates parsed candidate data before normalization."""

    EMAIL_PATTERN = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    PHONE_PATTERN = r"^(?:\+91)?[6-9]\d{9}$"

    LINKEDIN_PATTERN = (
        r"^https:\/\/(www\.)?linkedin\.com\/in\/[A-Za-z0-9_-]+\/?$"
    )

    def validate(self, profile: PartialCandidateProfile):

        errors = []

        # Name

        if not profile.full_name:
            errors.append({
                "field": "full_name",
                "message": "Missing candidate name.",
                "severity": "ERROR"
            })

        # Email

        for email in profile.emails:

            if not re.match(self.EMAIL_PATTERN, email):

                errors.append({
                    "field": "emails",
                    "message": f"Invalid email: {email}",
                    "severity": "ERROR"
                })

        # Phone

        for phone in profile.phones:

            if not re.match(self.PHONE_PATTERN, phone):

                errors.append({
                    "field": "phones",
                    "message": f"Invalid phone: {phone}",
                    "severity": "ERROR"
                })

        # LinkedIn

        if "linkedin" in profile.links:

            url = profile.links["linkedin"]

            if not re.match(self.LINKEDIN_PATTERN, url):

                errors.append({
                    "field": "links",
                    "message": "Invalid LinkedIn URL.",
                    "severity": "ERROR"
                })

        # Skills

        for skill in profile.skills:

            if not skill.strip():

                errors.append({
                    "field": "skills",
                    "message": "Empty skill detected.",
                    "severity": "WARNING"
                })

        # Experience

        if not isinstance(profile.experience, list):

            errors.append({
                "field": "experience",
                "message": "Experience should be a list.",
                "severity": "ERROR"
            })

        # Education

        if not isinstance(profile.education, list):

            errors.append({
                "field": "education",
                "message": "Education should be a list.",
                "severity": "ERROR"
            })

        return errors
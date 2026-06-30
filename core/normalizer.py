import phonenumbers

from models.partial_candidate import PartialCandidateProfile


class NormalizationEngine:
    """Normalizes candidate fields into a standard format."""

    SKILL_MAP = {
        "python": "Python",
        "java": "Java",
        "c++": "C++",
        "sql": "SQL",
        "machine learning": "Machine Learning",
        "deep learning": "Deep Learning",
        "tensorflow": "TensorFlow",
        "pytorch": "PyTorch",
        "javascript": "JavaScript",
        "react": "React",
        "node.js": "Node.js",
        "aws": "AWS",
        "docker": "Docker",
        "git": "Git",
        "html": "HTML",
        "css": "CSS"
    }

    def normalize(self, profile: PartialCandidateProfile):

        # Full Name

        if profile.full_name:
            profile.full_name = profile.full_name.strip().title()

        # Emails

        profile.emails = [
            email.strip().lower()
            for email in profile.emails
        ]

        # Phones

        normalized_phones = []

        for phone in profile.phones:

            try:
                parsed = phonenumbers.parse(phone, "IN")

                normalized = phonenumbers.format_number(
                    parsed,
                    phonenumbers.PhoneNumberFormat.E164
                )

                normalized_phones.append(normalized)

            except Exception:
                normalized_phones.append(phone)

        profile.phones = normalized_phones

        # Skills

        normalized_skills = set()

        for skill in profile.skills:

            cleaned = skill.strip()

            if not cleaned:
                continue

            normalized = self.SKILL_MAP.get(
                cleaned.lower(),
                cleaned.title()
            )

            normalized_skills.add(normalized)

        profile.skills = sorted(normalized_skills)

        # Location

        if profile.location:
            profile.location = profile.location.strip().title()

        return profile
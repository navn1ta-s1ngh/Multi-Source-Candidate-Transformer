# Resume parser placeholder
import re
import pdfplumber

from models.partial_candidate import PartialCandidateProfile
from utils.helpers import extract_email, extract_phone


class ResumeParser:
    """Extracts candidate information from a resume PDF."""
    
    SOURCE = "Resume"

    def __init__(self, file_path: str):

        self.file_path = file_path

    # Extract text

    def extract_text(self) -> str:

        text = ""

        try:
            with pdfplumber.open(self.file_path) as pdf:

                for page in pdf.pages:

                    page_text = page.extract_text()

                    if page_text:

                        text += page_text + "\n"
        except Exception:
            return ""

        return text

    # Extract name

    def extract_name(self, text):

        lines = text.split("\n")

        return lines[0].strip()

    # Extract skills

    def extract_skills(self, text):

        skills = []

        skill_keywords = [

            "Python",
            "Java",
            "C++",
            "SQL",
            "Machine Learning",
            "Deep Learning",
            "TensorFlow",
            "PyTorch",
            "JavaScript",
            "React",
            "Node.js",
            "AWS",
            "Docker",
            "Git"

        ]

        for skill in skill_keywords:

            if re.search(rf"\b{re.escape(skill)}\b", text, re.IGNORECASE):

                skills.append(skill)

        return skills

    # Extract education

    def extract_education(self, text):

        education = []

        if "University" in text or "College" in text:

            education.append({

                "raw": "Education detected"

            })

        return education

    # Extract experience

    def extract_experience(self, text):

        experience = []

        if "Intern" in text or "Engineer" in text:

            experience.append({

                "raw": "Experience detected"

            })

        return experience

    # Parse

    def parse(self):

        text = self.extract_text()

        profile = PartialCandidateProfile(

            source=self.SOURCE

        )

        profile.full_name = self.extract_name(text)

        email = extract_email(text)

        if email:

            profile.emails.append(email)

        phone = extract_phone(text)

        if phone:

            profile.phones.append(phone)

        profile.skills = self.extract_skills(text)

        profile.education = self.extract_education(text)

        profile.experience = self.extract_experience(text)

        return profile
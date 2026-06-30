# Notes parser placeholder
import re

from models.partial_candidate import PartialCandidateProfile


class NotesParser:
    """Extracts candidate information from recruiter notes."""

    SOURCE = "Recruiter Notes"

    def __init__(self, file_path: str):

        self.file_path = file_path

    # Read notes

    def read_notes(self):

        with open(self.file_path, "r", encoding="utf-8") as file:

            return file.read()

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

    # Extract location

    def extract_location(self, text):

        match = re.search(r"Location\s*:\s*(.*)", text, re.IGNORECASE)

        if match:

            return match.group(1).strip()

        return None

    # Parse

    def parse(self):

        text = self.read_notes()

        profile = PartialCandidateProfile(

            source=self.SOURCE

        )

        profile.skills = self.extract_skills(text)

        profile.location = self.extract_location(text)

        return profile
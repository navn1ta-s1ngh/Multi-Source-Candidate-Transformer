# LinkedIn parser placeholder
import json
import re

from models.partial_candidate import PartialCandidateProfile


class LinkedInParser:
    """Parses LinkedIn profile data into a PartialCandidateProfile."""

    SOURCE = "LinkedIn"

    def __init__(self, url_file: str, profile_file: str):

        self.url_file = url_file
        self.profile_file = profile_file

    # Read URL

    def read_url(self):

        with open(self.url_file, "r", encoding="utf-8") as file:

            return file.read().strip()

    # Validate URL

    def validate_url(self, url):

        pattern = r"^https:\/\/(www\.)?linkedin\.com\/in\/[A-Za-z0-9_-]+\/?$"

        return re.match(pattern, url) is not None

    # Load profile

    def load_profile(self):

        with open(self.profile_file, "r", encoding="utf-8") as file:

            return json.load(file)

    # Parse

    def parse(self):

        url = self.read_url()

        if not self.validate_url(url):

            raise ValueError("Invalid LinkedIn URL.")

        data = self.load_profile()

        profile = PartialCandidateProfile(

            source=self.SOURCE,

            full_name=data.get("fullName"),

            headline=data.get("headline"),

            location=data.get("location"),

            links={
                "linkedin": url
            },

            skills=data.get("skills", []),

            experience=data.get("experience", []),

            education=data.get("education", [])
        )

        return profile
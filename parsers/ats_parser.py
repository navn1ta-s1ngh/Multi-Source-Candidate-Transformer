import json

from models.partial_candidate import PartialCandidateProfile


class ATSParser:
    """Parses ATS JSON data into a PartialCandidateProfile."""

    SOURCE = "ATS"

    def __init__(self, file_path: str):

        self.file_path = file_path

    def parse(self):

        with open(self.file_path, "r", encoding="utf-8") as file:

            data = json.load(file)

        return PartialCandidateProfile(

            source=self.SOURCE,

            candidate_id=data.get("candidateId"),

            full_name=data.get("candidateName"),

            headline=data.get("headline"),

            emails=[data["primaryEmail"]] if data.get("primaryEmail") else [],

            phones=[data["primaryPhone"]] if data.get("primaryPhone") else [],

            location=data.get("location"),

            skills=data.get("skills", []),

            experience=data.get("experience", []),

            education=data.get("education", []),
        )
from typing import List

from models.partial_candidate import PartialCandidateProfile


class FieldMapper:
    """Maps parser outputs into a clean canonical partial profile."""

    def map(
        self,
        profiles: List[PartialCandidateProfile]
    ) -> List[PartialCandidateProfile]:

        mapped_profiles = []

        for profile in profiles:

            # Strings

            profile.full_name = (
                profile.full_name.strip()
                if profile.full_name
                else None
            )

            profile.headline = (
                profile.headline.strip()
                if profile.headline
                else None
            )

            profile.location = (
                profile.location.strip()
                if profile.location
                else None
            )

            # Lists

            profile.skills = list(set(profile.skills))

            profile.emails = list(set(profile.emails))

            profile.phones = list(set(profile.phones))

            mapped_profiles.append(profile)

        return mapped_profiles
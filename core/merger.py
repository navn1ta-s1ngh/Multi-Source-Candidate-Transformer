from typing import List

from models.partial_candidate import PartialCandidateProfile
from models.candidate import CandidateProfile


class MergeEngine:
    """Merges multiple partial profiles into one canonical candidate profile."""

    SOURCE_PRIORITY = {
        "Resume": 4,
        "LinkedIn": 3,
        "ATS": 2,
        "Recruiter Notes": 1
    }

    def merge(
        self,
        profiles: List[PartialCandidateProfile]
    ) -> CandidateProfile:

        candidate = CandidateProfile()

        # Higher priority profiles are processed first
        profiles = sorted(
            profiles,
            key=lambda p: self.SOURCE_PRIORITY.get(p.source, 0),
            reverse=True
        )

        # Identity

        for profile in profiles:

            if not candidate.full_name and profile.full_name:
                candidate.full_name = profile.full_name
                candidate.field_sources["full_name"] = [profile.source]

            if not candidate.candidate_id and profile.candidate_id:
                candidate.candidate_id = profile.candidate_id
                candidate.field_sources["candidate_id"] = [profile.source]

            if not candidate.headline and profile.headline:
                candidate.headline = profile.headline
                candidate.field_sources["headline"] = [profile.source]

            if not candidate.location and profile.location:
                candidate.location = profile.location
                candidate.field_sources["location"] = [profile.source]

        # Emails

        email_sources = set()

        for profile in profiles:
            if profile.emails:
                email_sources.add(profile.source)

            candidate.emails.extend(profile.emails)

        candidate.emails = sorted(list(set(candidate.emails)))
        candidate.field_sources["emails"] = sorted(list(email_sources))

        # Phones

        phone_sources = set()

        for profile in profiles:
            if profile.phones:
                phone_sources.add(profile.source)

            candidate.phones.extend(profile.phones)

        candidate.phones = sorted(list(set(candidate.phones)))
        candidate.field_sources["phones"] = sorted(list(phone_sources))

        # Links

        link_sources = set()

        for profile in profiles:
            if profile.links:
                link_sources.add(profile.source)

            candidate.links.update(profile.links)

        candidate.field_sources["links"] = sorted(list(link_sources))

        # Skills

        skill_sources = set()

        for profile in profiles:
            if profile.skills:
                skill_sources.add(profile.source)

            candidate.skills.extend(profile.skills)

        candidate.skills = sorted(list(set(candidate.skills)))
        candidate.field_sources["skills"] = sorted(list(skill_sources))

        # Experience

        experience_sources = set()

        for profile in profiles:
            if profile.experience:
                experience_sources.add(profile.source)

            candidate.experience.extend(profile.experience)

        candidate.field_sources["experience"] = sorted(
            list(experience_sources)
        )

        # Education

        education_sources = set()

        for profile in profiles:
            if profile.education:
                education_sources.add(profile.source)

            candidate.education.extend(profile.education)

        candidate.field_sources["education"] = sorted(
            list(education_sources)
        )

        return candidate
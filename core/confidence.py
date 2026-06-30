from models.candidate import CandidateProfile


class ConfidenceEngine:
    """Computes confidence scores using source agreement."""

    CONFIDENCE_MAP = {
        1: 0.70,
        2: 0.85,
        3: 0.95,
        4: 1.00
    }

    def compute(self, candidate: CandidateProfile):

        for field, sources in candidate.field_sources.items():

            count = len(sources)

            candidate.field_confidence[field] = self.CONFIDENCE_MAP.get(
                count,
                1.00
            )

        return candidate

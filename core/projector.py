import json
from pathlib import Path

from models.candidate import CandidateProfile


class ProjectionEngine:
    """Projects the canonical profile into a configurable output schema."""

    def __init__(
        self,
        config_path: str,
        output_path: str = "output/default_candidate.json"
    ):

        self.config_path = config_path
        self.output_path = self._resolve_output_path(output_path)

    def _resolve_output_path(self, output_path: str) -> Path:
        project_root = Path(__file__).resolve().parent.parent
        path = Path(output_path)

        if path.is_absolute():
            return path

        return project_root / path

    def project(self, candidate: CandidateProfile):

        # Read projection configuration
        with open(self.config_path, "r", encoding="utf-8") as file:
            config = json.load(file)

        fields = config.get("fields", [])

        candidate_dict = candidate.model_dump()

        projected = {}

        for field in fields:
            if field in candidate_dict:
                projected[field] = candidate_dict[field]

        # Ensure output directory exists
        self.output_path.parent.mkdir(parents=True, exist_ok=True)

        # Save projected JSON
        with open(self.output_path, "w", encoding="utf-8") as file:
            json.dump(projected, file, indent=4)

        return projected
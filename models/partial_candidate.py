from typing import List, Dict, Any, Optional
from pydantic import BaseModel, Field


class PartialCandidateProfile(BaseModel):
    """Canonical representation of candidate data extracted from a single source."""

    source: str

    candidate_id: Optional[str] = None

    full_name: Optional[str] = None

    headline: Optional[str] = None

    emails: List[str] = Field(default_factory=list)

    phones: List[str] = Field(default_factory=list)

    location: Optional[str] = None

    links: Dict[str, str] = Field(default_factory=dict)

    skills: List[str] = Field(default_factory=list)

    experience: List[Dict[str, Any]] = Field(default_factory=list)

    education: List[Dict[str, Any]] = Field(default_factory=list)
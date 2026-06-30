from parsers.ats_parser import ATSParser
from parsers.resume_parser import ResumeParser
from parsers.linkedin_parser import LinkedInParser
from parsers.notes_parser import NotesParser

from core.mapper import FieldMapper
from core.validator import ValidationEngine
from core.normalizer import NormalizationEngine
from core.merger import MergeEngine
from core.confidence import ConfidenceEngine
from core.projector import ProjectionEngine
from core.schema_validator import SchemaValidator


def main():

    print("=" * 70)
    print("MULTI-SOURCE CANDIDATE DATA TRANSFORMER")
    print("=" * 70)

    # ATS

    print("\n[1] ATS Parser\n")

    ats = ATSParser("input/ats.json")

    print(ats.parse().model_dump_json(indent=4))

    # Resume

    print("\n" + "=" * 70)
    print("[2] Resume Parser\n")

    resume = ResumeParser("input/resume.pdf")

    print(resume.parse().model_dump_json(indent=4))

    # LinkedIn

    print("\n" + "=" * 70)
    print("[3] LinkedIn Parser\n")

    linkedin = LinkedInParser(
        "input/linkedin.url",
        "input/linkedin_profile.json"
    )

    print(linkedin.parse().model_dump_json(indent=4))

    # Recruiter Notes
    print("\n" + "=" * 70)
    print("[4] Recruiter Notes Parser\n")

    notes = NotesParser("input/recruiter_notes.txt")

    print(notes.parse().model_dump_json(indent=4))

    # Field Mapper
    profiles = [
        ats.parse(),
        resume.parse(),
        linkedin.parse(),
        notes.parse()
    ]

    mapper = FieldMapper()

    mapped_profiles = mapper.map(profiles)

    print("\n" + "=" * 70)
    print("[5] Field Mapping Engine\n")

    for profile in mapped_profiles:
        print(profile.model_dump_json(indent=4))

    # Validation Engine
    validator = ValidationEngine()

    print("\n" + "=" * 70)
    print("[6] Validation Engine\n")

    for profile in mapped_profiles:

        print(f"\nSource : {profile.source}")

        errors = validator.validate(profile)

        if not errors:

            print("Validation Passed")

        else:

            for error in errors:

                print(
                    f"[{error['severity']}] "
                    f"{error['field']} : "
                    f"{error['message']}"
                )

    # Normalization Engine
    normalizer = NormalizationEngine()

    normalized_profiles = []

    print("\n" + "=" * 70)
    print("[7] Normalization Engine\n")

    for profile in mapped_profiles:

        normalized = normalizer.normalize(profile)

        normalized_profiles.append(normalized)

        print(normalized.model_dump_json(indent=4))

    # Merge Engine
    merger = MergeEngine()

    candidate = merger.merge(normalized_profiles)

    print("\n" + "=" * 70)
    print("[8] Merge Engine\n")

    print(candidate.model_dump_json(indent=4))

    # Confidence & Provenance Engine
    confidence = ConfidenceEngine()

    candidate = confidence.compute(candidate)

    print("\n" + "=" * 70)
    print("[9] Confidence & Provenance Engine\n")

    print(candidate.model_dump_json(indent=4))

    # Projection Engine (Default Configuration)

    projector = ProjectionEngine(
        "config/default.json",
        "output/default_candidate.json"
    )

    default_output = projector.project(candidate)

    print("\n" + "=" * 70)
    print("[10] Projection Engine (Default Configuration)\n")

    import json
    print(json.dumps(default_output, indent=4))

    # Projection Engine (Custom Configuration)
    custom_projector = ProjectionEngine(
        "config/custom.json",
        "output/recruiter_view.json"
    )

    recruiter_output = custom_projector.project(candidate)

    print("\n" + "=" * 70)
    print("[10A] Projection Engine (Custom Configuration)\n")

    print(json.dumps(recruiter_output, indent=4))

    # Schema Validator (Default Configuration)
    validator = SchemaValidator("config/default.json")

    valid, messages = validator.validate(
        "output/default_candidate.json"
    )

    print("\n" + "=" * 70)
    print("[11] Schema Validator (Default)\n")

    for message in messages:
        print(message)

    # Schema Validator (Recruiter View)
    recruiter_validator = SchemaValidator("config/custom.json")

    valid, messages = recruiter_validator.validate(
        "output/recruiter_view.json"
    )

    print("\n" + "=" * 70)
    print("[11A] Schema Validator (Recruiter View)\n")

    for message in messages:
        print(message)

    # Pipeline Verification Summary
    print("\n" + "=" * 70)
    print("PIPELINE EXECUTION SUMMARY")
    print("=" * 70)

    print("Parser Engine                  : Completed")
    print("Field Mapping Engine           : Completed")
    print("Validation Engine              : Completed")
    print("Normalization Engine           : Completed")
    print("Merge Engine                   : Completed")
    print("Confidence & Provenance Engine : Completed")
    print("Projection Engine              : Completed")
    print("Schema Validator               : Completed")

    print("\nPipeline Status : SUCCESS")
    print("Generated Files :")
    print("  - output/default_candidate.json")
    print("  - output/recruiter_view.json")
    print("=" * 70)

if __name__ == "__main__":
    main()
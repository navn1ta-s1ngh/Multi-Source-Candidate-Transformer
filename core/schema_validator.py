import json
import os


class SchemaValidator:
    """Validates the generated JSON against the configured schema."""

    def __init__(self, config_path: str):

        self.config_path = config_path

    def validate(self, output_path: str):

        # Output file exists

        if not os.path.exists(output_path):

            return False, ["Output JSON file not found."]

        # Read configuration

        with open(self.config_path, "r", encoding="utf-8") as file:

            config = json.load(file)

        required_fields = config.get("fields", [])

        # Read output JSON

        try:

            with open(output_path, "r", encoding="utf-8") as file:

                output = json.load(file)

        except json.JSONDecodeError:

            return False, ["Output file is not valid JSON."]

        # Validate required fields

        errors = []

        for field in required_fields:

            if field not in output:

                errors.append(f"Missing required field: {field}")

        if errors:

            return False, errors

        return True, ["Schema validation passed."]
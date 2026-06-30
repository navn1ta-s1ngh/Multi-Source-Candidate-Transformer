# Multi-Source Candidate Data Transformer

A configurable data transformation pipeline that consolidates heterogeneous candidate information from multiple sources into a validated canonical candidate profile with configurable output projection.

**Author:** Navnita Naresh Singh  
**Program:** B.Tech Computer Science Engineering (Mathematics & Computing)  
**Institution:** Netaji Subhas University of Technology (NSUT)

---

## Project Overview

Modern recruiting systems receive candidate information from multiple independent sources such as Applicant Tracking Systems (ATS), resumes, LinkedIn profiles, and recruiter notes. These sources often contain duplicate, conflicting, incomplete, or differently formatted information.

This project implements a modular transformation pipeline that:

- Ingests heterogeneous candidate data
- Maps different source schemas into a canonical representation
- Validates and normalizes extracted information
- Resolves conflicts using deterministic merge policies
- Tracks provenance for every merged field
- Computes confidence scores based on source agreement
- Generates configurable output JSON without changing application code
- Validates the generated output before completion

The implementation follows a modular engine-based architecture where each processing stage has a single responsibility.

---

# System Architecture


The transformation pipeline consists of eight sequential engines:

1. Parser Engine
2. Field Mapping Engine
3. Validation Engine
4. Normalization Engine
5. Entity Resolution & Merge Engine
6. Confidence & Provenance Engine
7. Projection Engine
8. Schema Validator

---

# Supported Input Sources

The pipeline currently supports four heterogeneous candidate information sources.

| Source | Type |
|---------|------|
| ATS JSON | Structured |
| Resume PDF | Unstructured |
| LinkedIn Profile URL | Unstructured |
| Recruiter Notes (.txt) | Unstructured |

Each source is parsed independently before entering the canonical transformation pipeline.

---

# Processing Pipeline

```
ATS JSON
Resume PDF
LinkedIn URL
Recruiter Notes
        │
        ▼
Parser Engine
        │
        ▼
Field Mapping Engine
        │
        ▼
Validation Engine
        │
        ▼
Normalization Engine
        │
        ▼
Entity Resolution & Merge Engine
        │
        ▼
Confidence & Provenance Engine
        │
        ▼
Projection Engine
        │
        ▼
Schema Validator
        │
        ▼
Canonical Candidate JSON
```

---

# Project Structure

```text
candidate-transformer/
│
├──.gitignore
├── main.py
├── README.md
├── requirements.txt
│
├── input/
│   ├── ats.json
│   ├── resume.pdf
│   ├── linkedin.url
│   └── linkedin_profile.json
│   └── recruiter_notes.txt 
│   
├── output/
│   ├── default_candidate.json
│   └── recruiter_view.json
│
├── config/
│   ├── default.json
│   └── custom.json
│
├── parsers/
│   ├── ats_parser.py
│   ├── resume_parser.py
│   ├── linkedin_parser.py
│   └── notes_parser.py
│
├── core/
│   ├── mapper.py
│   ├── validator.py
│   ├── normalizer.py
│   ├── merger.py
│   ├── confidence.py
│   ├── projector.py
│   └── schema_validator.py
│
├── models/
│   ├── partial_candidate.py
│   └── candidate.py
│
└── utils/
    └── helpers.py
```

---

# Canonical Output Schema

The pipeline generates a unified candidate profile containing:

- Candidate ID
- Full Name
- Headline
- Email Addresses
- Phone Numbers
- Location
- External Links
- Skills
- Experience
- Education
- Source Provenance
- Field Confidence Scores

---

# Merge Policy

Conflicting values are resolved using deterministic source priorities.

| Field | Priority |
|--------|----------|
| Name | Resume → LinkedIn → ATS |
| Headline | LinkedIn → Resume |
| Contact Information | Resume → ATS |
| Location | LinkedIn → Resume → ATS → Recruiter Notes |
| Skills | Union of all sources |
| Experience | Combined across all sources |
| Education | Resume → LinkedIn → ATS |

This strategy prioritizes trusted structured information while preserving complementary information from additional sources.

---

# Confidence & Provenance

Every merged field records:

- Source(s) contributing to the final value
- Confidence score based on source agreement

Confidence increases as multiple independent sources agree on the same information.

---

# Runtime Configurable Output

The Projection Engine reads a runtime configuration file to determine the output schema.

Two configurations are included:

### Default Configuration

```
config/default.json
```

Generates the complete canonical candidate profile.

Output:

```
output/default_candidate.json
```

### Recruiter View

```
config/custom.json
```

Projects only recruiter-relevant fields without modifying the pipeline implementation.

Output:

```
output/recruiter_view.json
```

This demonstrates runtime-configurable output using the same transformation pipeline.

---

# Technologies Used

- Python 3
- Pydantic
- pdfplumber
- phonenumbers
- JSON
- Regular Expressions

---

# Running the Project

## 1. Clone the repository

```bash
git clone https://github.com/navn1ta-s1ngh/Multi-Source-Candidate-Transformer.git
cd Multi-Source-Candidate-Transformer
```

## 2. Create a virtual environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

## 4. Prepare the input files

Place the following files inside the `input/` directory:

```
input/
├── ats.json
├── resume.pdf
├── linkedin.txt
└── recruiter_notes.txt
```

Example input files are included in this repository.

## 5. Execute the pipeline

```bash
python main.py
```

(If `python` is not available, use `python3 main.py`.)

## 6. Generated outputs

The pipeline executes all transformation engines and generates:

```
output/
├── default_candidate.json
└── recruiter_view.json
```

During execution, the terminal displays the status of each processing engine along with schema validation results.

# Example Outputs

The project generates two outputs.

### Default Candidate Profile

A complete canonical candidate profile containing all supported fields.

### Recruiter View

A recruiter-focused projection containing only selected fields defined by the runtime configuration.

---

# Design Decisions

Some key design choices include:

- Modular engine-based architecture
- Canonical intermediate data model
- Deterministic merge policy
- Source provenance tracking
- Explainable confidence scoring
- Runtime-configurable output projection
- Independent schema validation

---

# Edge Cases Handled

The pipeline gracefully handles:

- Missing input sources
- Duplicate candidate information
- Invalid email and phone formats
- Malformed LinkedIn URLs
- Missing or conflicting candidate fields

Unknown values are preserved as missing rather than being inferred.

---

# Future Improvements

Potential production enhancements include:

- LinkedIn API integration
- ATS connector integrations
- OCR support for scanned resumes
- ML-based confidence scoring
- Advanced entity resolution
- REST API deployment
- Cloud-native execution
- Batch candidate processing

---


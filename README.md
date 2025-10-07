# The Great Refactor: Empirical Data

Supporting data for ["The Great Refactor: How AI Is Rewriting the Cognitive Code of Work"](link-to-essay)

## Overview

This repository contains systematic analysis of 47 verified enterprise AI implementations across banking, healthcare, manufacturing, government, and other sectors. The dataset challenges widely-circulated claims of 90%+ AI failure rates and identifies specific patterns that separate successful integration from catastrophic failure.

**Key finding:** Approximately 75% of well-designed AI initiatives deliver measurable value, while 9% fail catastrophically. The difference isn't technology—it's integration architecture.

## Repository Structure

```
├── data/                              # Raw datasets
│   ├── Master_AI_Case_Studies_Consolidated.csv
│   └── Emblematic_Cases_Analysis.csv
├── analysis/                          # Analytical findings
│   └── AI_Adoption_Taxonomy_Synthesis.md
└── sources/                           # Bibliography and source links
    └── BIBLIOGRAPHY.md
```

## Dataset

**`Master_AI_Case_Studies_Consolidated.csv`** — 47 verified enterprise AI implementations coded across 22 fields:
- Organization, sector, geography, size
- Process type, function, AI modality
- Integration depth, data posture, controls
- Vendor vs. in-house, maturity stage
- Intended outcomes, observed results
- Change management, risk/compliance
- Cost-benefit analysis, implementation status
- Pattern tags and source citations

See [`data/DATA_DICTIONARY.md`](data/DATA_DICTIONARY.md) for complete field definitions and usage examples.

**`Emblematic_Cases_Analysis.csv`** — Subset of 12 most illustrative cases spanning success (Klarna, Netflix, VA Healthcare) to catastrophic failure (Watson Oncology, McDonald's AI drive-thru, Amazon resume screening)

**Note:** Source citations in the CSVs currently use descriptive labels (e.g., "Multiple sources"). For full verifiability, we recommend cross-referencing with [`sources/BIBLIOGRAPHY.md`](sources/BIBLIOGRAPHY.md) which contains actual source links and publication details.

## Methodology

All case studies drawn from publicly verifiable sources:
- Government disclosures (VA AI Use Case Inventory)
- Industry research (Gartner 2024-2025, McKinsey State of AI 2024, Deloitte State of GenAI Q4 2024, Stanford HAI AI Index 2025)
- Company-disclosed implementations with named organizations and quantified outcomes

See [`analysis/AI_Adoption_Taxonomy_Synthesis.md`](analysis/AI_Adoption_Taxonomy_Synthesis.md) for complete coding framework, confidence assessments, and pattern analysis.

## Key Findings

1. **Success rate varies by organizational maturity:** High-maturity organizations achieve 54% pilot-to-production success vs. 20% for low-maturity organizations (Gartner 2024-2025)

2. **Four predictable failure modes:** Over-delegation + anthropomorphism, over-delegation + deterministic expectations, under-delegation + software mindset, under-delegation + analysis paralysis

3. **Integration architecture matters more than technology:** Organizations using similar AI capabilities, vendors, and talent achieve radically different outcomes based on how they design human-AI integration

4. **Most organizations stuck at pilot scale:** The "GenAI Divide" isn't about model quality—it's about bridging from experimentation to production-scale integration

See [`analysis/AI_Adoption_Taxonomy_Synthesis.md`](analysis/AI_Adoption_Taxonomy_Synthesis.md) for detailed pattern breakdown, sector analysis, and success factors.

## Citation

If you use this data in research or analysis, please cite:

```
Whatcott, J. (2025). The Great Refactor: How AI Is Rewriting the Cognitive Code of Work.
Retrieved from https://github.com/sigma512/great-refactor-data
```

## Contributing

Found an error or have additional verified case studies? Please file an issue or submit a pull request. All contributions must include:
- Named organization
- Publicly verifiable source
- Quantified outcomes (where available)

## License

This work is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — you're free to use with attribution.

---

**Author:** Jeff Whatcott  
**Contact:** jeff@whatcott.com
**Last updated:** October 2025

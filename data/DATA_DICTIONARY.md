# Data Dictionary: Master AI Case Studies

## Field Definitions

### Organizational Dimensions

**Organization** — Name of the implementing organization  
*Example: Klarna, JPMorgan Chase, VA Healthcare*

**Sector** — Primary industry classification  
*Values: Fintech, Banking, Healthcare, Manufacturing, Government, Telecom, Retail, etc.*

**Geography** — Primary operational geography  
*Values: USA, Global, UK, EU, etc.*

**Size** — Organization scale  
*Values: Enterprise (>1000 employees), Mid-market (100-1000), SMB (<100)*

### Process and Technical Dimensions

**Process** — Specific business process being augmented or automated  
*Example: "End-to-end customer service chat handling," "Transaction monitoring and fraud detection"*

**Function** — Business function category  
*Values: Customer Operations, Risk & Compliance, Clinical, Manufacturing, Supply Chain, etc.*

**AI_Modality** — Type of AI technology deployed  
*Values:*
- Generative AI (LLM)
- ML/AI Platform
- Computer Vision (CV)
- Hybrid (ML + GenAI)
- ASR (Automatic Speech Recognition)
- Predictive ML

**Integration_Depth** — Level of AI integration into workflow  
*Scale from assistive to autonomous:*
- Assistive drafting / Decision support
- Human-in-the-loop (HITL) automation
- Straight-through processing (for simple cases)
- Agentic orchestration
- Platform + governance

### Implementation Characteristics

**Data_Posture** — Nature of data being processed  
*Examples: "Structured customer data," "Medical imaging data," "Transaction and customer data"*

**Controls** — Oversight and governance mechanisms  
*Examples: "HITL escalation for complex cases," "Real-time monitoring," "FDA clearance and clinical oversight"*

**Vendor_vs_Inhouse** — Technology sourcing approach  
*Values: Vendor partnership, In-house platform, In-house + vendor, Vendor implementation*

**Maturity** — Implementation stage  
*Values:*
- Pilot
- Active pilot
- Limited production
- Production
- Broad production
- Production rollout
- National rollout

**Start_Date** — Implementation start date  
*Format: YYYY or YYYY-MM*

### Outcomes and Performance

**Intended_Outcome** — Stated goals and objectives  
*Example: "Increase self-service containment; reduce agent load while maintaining CSAT"*

**Observed_Results** — Measured outcomes and impacts  
*Example: "~2/3 of chats handled by AI, $40M annual savings"*

**Change_Mgmt** — Change management and training requirements  
*Example: "Staff retraining and role evolution," "Agent training on new workflows"*

**Risk_Compliance** — Regulatory and compliance considerations  
*Example: "FDA compliance and patient safety," "Financial regulation compliance"*

**Cost_Benefit** — Financial impact  
*Examples: "$40M annual cost savings," "$1.5B cost savings," "Significant operational savings reported"*

**Status** — Current implementation status  
*Values: Live, Active pilot, Ongoing, Scaling, Production rollout*

### Metadata

**Pattern_Tags** — Success factors or failure patterns identified  
*Example: "Clear problem framing, measurable KPI, executive sponsorship"*

**Source_Platform** — Research platform(s) used for case documentation  
*Values: ChatGPT, Claude, Gemini, Perplexity, or combinations*

**Source_Citation** — Source attribution  
*Examples: "Multiple sources," "VA AI Use Case Inventory," "Press coverage," "Financial publications"*

---

## Data Quality Notes

### Confidence Levels

Cases are drawn from sources with varying confidence levels:

- **High Confidence**: Government disclosures, peer-reviewed research, verified business publications with named organizations and quantified outcomes
- **Medium Confidence**: Vendor case studies with customer attribution, consulting firm analysis
- **Low Confidence**: Estimated ranges, observational patterns (marked in Pattern_Tags)

### Missing Data

- Empty fields indicate information not publicly available
- "Reported" or "Significant" in Cost_Benefit indicates qualitative rather than quantified outcomes
- Date precision varies based on source disclosure

### Updates

This dataset reflects information available as of January 2025. Organizations may have progressed beyond documented maturity stages.

---

## Usage Examples

### Filter by success pattern
```python
import pandas as pd
df = pd.read_csv('Master_AI_Case_Studies_Consolidated.csv')

# Find cases with measurable cost savings
successful = df[df['Cost_Benefit'].str.contains('M|B', na=False)]

# Find cases at production scale
production = df[df['Maturity'].str.contains('production', case=False, na=False)]
```

### Analyze by sector
```python
# Group by sector and count
sector_counts = df.groupby('Sector').size().sort_values(ascending=False)

# Success rate by sector (cases with quantified benefits)
df['has_quantified_benefit'] = df['Cost_Benefit'].str.contains(r'\$\d+', na=False)
success_by_sector = df.groupby('Sector')['has_quantified_benefit'].mean()
```

### Integration depth analysis
```python
# Distribution of integration approaches
integration_dist = df['Integration_Depth'].value_counts()

# Correlation between integration depth and maturity
depth_maturity = pd.crosstab(df['Integration_Depth'], df['Maturity'])
```

---

For complete methodology and pattern analysis, see [`AI_Adoption_Taxonomy_Synthesis.md`](../analysis/AI_Adoption_Taxonomy_Synthesis.md)

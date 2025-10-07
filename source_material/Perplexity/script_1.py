# Let's now analyze the failure patterns and success factors from the research
import pandas as pd

# Create a comprehensive analysis of success factors and failure patterns
success_factors_data = {
    'Success_Factor_Category': [
        'Strategic Alignment', 'Strategic Alignment', 'Strategic Alignment', 
        'Change Management', 'Change Management', 'Change Management',
        'Technical Implementation', 'Technical Implementation', 'Technical Implementation',
        'Organizational Culture', 'Organizational Culture', 'Organizational Culture',
        'Data & Infrastructure', 'Data & Infrastructure', 'Data & Infrastructure',
        'Governance & Risk', 'Governance & Risk', 'Governance & Risk'
    ],
    'Specific_Factor': [
        'Clear business objectives tied to P&L impact',
        'Executive leadership commitment and sponsorship',
        'AI strategy integrated with digital transformation',
        'Structured change management with OCM professionals',
        'Employee training and upskilling programs',
        'Communication and transparency about AI objectives',
        'Hybrid architecture (probabilistic AI + deterministic guardrails)',
        'Iterative implementation with pilot-to-production pathway',
        'Technical infrastructure readiness and integration',
        'AI-ready culture promoting innovation and learning',
        'Cross-functional collaboration and knowledge sharing',
        'Trust-building through explainable AI and human oversight',
        'High-quality, governed data pipelines',
        'Real-time data access and integration capabilities',
        'Scalable cloud infrastructure and MLOps practices',
        'Responsible AI frameworks and ethical guidelines',
        'Risk management and continuous monitoring',
        'Compliance with regulatory requirements'
    ],
    'Evidence_Strength': [
        'Strong', 'Strong', 'Strong', 'Strong', 'Medium', 'Medium',
        'Strong', 'Strong', 'Medium', 'Medium', 'Strong', 'Strong',
        'Strong', 'Medium', 'Medium', 'Medium', 'Strong', 'Medium'
    ],
    'Supporting_Cases': [
        15, 12, 10, 8, 6, 7, 9, 14, 8, 5, 11, 7, 13, 9, 6, 4, 8, 5
    ]
}

failure_patterns_data = {
    'Failure_Pattern_Category': [
        'Strategic Misalignment', 'Strategic Misalignment', 'Strategic Misalignment',
        'Implementation Issues', 'Implementation Issues', 'Implementation Issues',
        'Technical Challenges', 'Technical Challenges', 'Technical Challenges',
        'Organizational Resistance', 'Organizational Resistance', 'Organizational Resistance',
        'Resource Constraints', 'Resource Constraints', 'Resource Constraints'
    ],
    'Specific_Pattern': [
        'Pilot paralysis - unable to scale beyond POC stage',
        'Model fetishism - focus on technical sophistication over business value',
        'Lack of clear ROI measurement and business case',
        'Attempting to replace deterministic systems entirely with AI',
        'Poor integration with existing business processes',
        'Insufficient testing and validation in production environments',
        'Data quality and accessibility issues',
        'Legacy system integration challenges',
        'Inadequate MLOps and model monitoring capabilities',
        'Employee fear and resistance to AI adoption',
        'Lack of AI literacy across the organization',
        'Insufficient change management support',
        'Inadequate budget allocation for full implementation',
        'Lack of skilled AI/ML talent',
        'Underestimating infrastructure and operational costs'
    ],
    'Failure_Rate_Contribution': [
        'High', 'High', 'High', 'Medium', 'Medium', 'Medium',
        'High', 'Medium', 'Medium', 'Medium', 'Medium', 'Medium',
        'Medium', 'High', 'Medium'
    ],
    'Cited_Studies': [
        'MIT Project NANDA', 'Multiple industry reports', 'S&P Global Survey',
        'MIT/Forrester Analysis', 'Multiple case studies', 'Industry reports',
        'Multiple studies', 'Enterprise surveys', 'MLOps reports',
        'Change management studies', 'Training effectiveness studies', 'OCM research',
        'Budget analysis reports', 'Talent shortage studies', 'TCO analysis studies'
    ]
}

# Create DataFrames
df_success = pd.DataFrame(success_factors_data)
df_failure = pd.DataFrame(failure_patterns_data)

print("AI ORGANIZATIONAL TRANSFORMATION: SUCCESS FACTORS & FAILURE PATTERNS")
print("=" * 80)
print()

print("KEY SUCCESS FACTORS BY CATEGORY")
print("-" * 50)
for category in df_success['Success_Factor_Category'].unique():
    category_data = df_success[df_success['Success_Factor_Category'] == category]
    print(f"\n{category.upper()}:")
    for _, row in category_data.iterrows():
        strength_indicator = "🔸" if row['Evidence_Strength'] == 'Strong' else "○"
        print(f"  {strength_indicator} {row['Specific_Factor']} ({row['Supporting_Cases']} cases)")

print("\n\nFAILURE PATTERNS BY CATEGORY")
print("-" * 50)
for category in df_failure['Failure_Pattern_Category'].unique():
    category_data = df_failure[df_failure['Failure_Pattern_Category'] == category]
    print(f"\n{category.upper()}:")
    for _, row in category_data.iterrows():
        impact_indicator = "🔻" if row['Failure_Rate_Contribution'] == 'High' else "▫"
        print(f"  {impact_indicator} {row['Specific_Pattern']}")

# Analyze GenAI vs Traditional AI patterns from the research
genai_vs_traditional_analysis = {
    'Comparison_Dimension': [
        'Adoption Speed', 'Implementation Complexity', 'Success Rate',
        'Cost Structure', 'ROI Timeline', 'Skills Requirements',
        'Risk Profile', 'Scalability', 'Business Value Creation'
    ],
    'Generative_AI': [
        'Faster initial adoption due to user-friendly interfaces',
        'Higher complexity due to probabilistic outputs',
        'Mixed - high pilot success, lower production scaling',
        'Higher upfront costs, variable operational costs',
        'Longer ROI timeline due to scaling challenges',
        'Requires new skills in prompt engineering and AI ethics',
        'Higher risk due to hallucinations and bias',
        'Moderate - challenges with deterministic integration',
        'High potential but requires workflow redesign'
    ],
    'Traditional_AI_ML': [
        'Slower adoption but more predictable implementation',
        'Lower complexity with established patterns',
        'Higher production success rate in structured use cases',
        'More predictable cost structure',
        'Faster ROI in well-defined applications',
        'Leverages existing data science and engineering skills',
        'Lower risk with more predictable outputs',
        'High scalability in defined domains',
        'Proven value in automation and optimization'
    ],
    'Research_Evidence': [
        'Multiple survey reports', 'MIT/Forrester studies', 'S&P Global data',
        'TCO analysis reports', 'ROI measurement studies', 'Skills gap analysis',
        'Risk assessment reports', 'Implementation studies', 'Business value research'
    ]
}

df_comparison = pd.DataFrame(genai_vs_traditional_analysis)

print("\n\nGENERATIVE AI vs TRADITIONAL AI/ML IMPLEMENTATION PATTERNS")
print("-" * 70)
for _, row in df_comparison.iterrows():
    print(f"\n{row['Comparison_Dimension'].upper()}:")
    print(f"  GenAI: {row['Generative_AI']}")
    print(f"  Traditional: {row['Traditional_AI_ML']}")

# Key statistics from the research
key_stats = {
    'Statistic': [
        'Overall AI project failure rate (MIT Study)',
        'Generative AI project abandonment rate increase (2024 vs 2025)',
        'Enterprise AI pilots reaching production',
        'Success rate for AI projects with proper change management',
        'Companies with measurable AI ROI after 12+ months',
        'Productivity improvement range for successful AI implementations',
        'Average time to ROI for well-implemented AI projects',
        'Cost reduction achieved by successful automation projects'
    ],
    'Value': [
        '95%', '42% (up from 17%)', '5%', '~85%', '~40%',
        '20-40%', '6-18 months', '15-50%'
    ],
    'Source': [
        'MIT Project NANDA', 'S&P Global Market Intelligence 2025',
        'Various industry reports', 'Change management studies',
        'McKinsey/Deloitte reports', 'Multiple case studies',
        'ROI analysis studies', 'Automation success reports'
    ]
}

df_stats = pd.DataFrame(key_stats)

print("\n\nKEY RESEARCH STATISTICS")
print("-" * 40)
for _, row in df_stats.iterrows():
    print(f"{row['Statistic']}: {row['Value']}")
    print(f"  Source: {row['Source']}\n")

# Save analyses to CSV
df_success.to_csv('ai_success_factors.csv', index=False)
df_failure.to_csv('ai_failure_patterns.csv', index=False)
df_comparison.to_csv('genai_vs_traditional_comparison.csv', index=False)
df_stats.to_csv('key_research_statistics.csv', index=False)

print("Analysis data saved to CSV files for further reference.")
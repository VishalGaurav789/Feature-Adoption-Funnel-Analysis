# Feature Adoption & Funnel Analysis

A beginner-friendly product analytics project that analyzes user events, account activity, and transactions to understand feature adoption, conversion drop-offs, engagement patterns, and repeat usage.

## Project Goal
This project simulates a product analytics workflow where we answer questions such as:
- How many users start and complete key product actions?
- Where are the biggest drop-offs in the funnel?
- Which user segments are most engaged?
- Which features are adopted the most over time?

## Tech Stack
- Python
- SQL
- Pandas
- Matplotlib
- Power BI (dashboard plan included)

## Folder Structure
```text
feature-adoption-funnel-analysis/
|-- data/
|   |-- raw/
|   |   |-- users.csv
|   |   |-- accounts.csv
|   |   `-- events.csv
|-- sql/
|   |-- schema.sql
|   `-- funnel_analysis.sql
|-- src/
|   |-- generate_sample_data.py
|   `-- analyze_funnel.py
|-- outputs/
|   |-- funnel_stage_summary.csv
|   |-- feature_adoption_summary.csv
|   `-- funnel_dropoff_chart.png
|-- dashboard/
|   `-- powerbi_guide.md
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Key Analysis Covered
- Funnel stage counts and conversion rate
- Drop-off between onboarding and feature completion
- Feature usage by event type
- Activation and repeat usage view
- Simple engagement segmentation

## How to Run
```bash
pip install -r requirements.txt
python src/generate_sample_data.py
python src/analyze_funnel.py
```

## Suggested Dashboard Pages
1. Funnel overview
2. Feature adoption trend
3. Activation and repeat usage summary
4. Low-conversion stage monitoring

## Resume Alignment
This repository supports a resume narrative around:
- Feature adoption analysis
- Funnel analysis
- KPI reporting
- User behavior analysis
- Product performance monitoring

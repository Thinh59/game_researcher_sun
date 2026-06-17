---
name: market-researcher
description: "Use this skill to evaluate market viability, Total Addressable Market (TAM), and forecast Key Performance Indicators (KPIs) for a specific game genre in a designated region."
---

# Market Research & KPI Forecaster

Version: 1.0.0

## Trigger Conditions

Use this skill when the task requires evaluating the business viability of a game concept before development begins. This includes demographic breakdowns, regional market sizing, and projecting financial/engagement KPIs.

Do not use this skill for game mechanics, UI/UX evaluation, or in-game economy tuning.

Rely strictly on credible industry data sources (e.g., SensorTower, Data.ai, Newzoo benchmarks) when available, and explicitly mark estimations.

## Process

1. Start with a BLUF (Bottom Line Up Front): A 2-3 sentence executive summary on whether the market is viable.
2. Define the Target Market Segment:
   - Identify the primary demographic based on `{{TARGET_AUDIENCE}}`.
   - Assess the market saturation for `{{GAME_GENRE}}` in `{{TARGET_REGION}}`.
3. Forecast Critical KPIs:
   - Estimate CPI (Cost Per Install).
   - Estimate Retention Rates (D1, D7, D30).
   - Estimate ARPDAU (Average Revenue Per Daily Active User).
4. Identify Key Market Trends & Risks.

## Output Template

```markdown
## BLUF
[Executive summary of market feasibility for the genre in the region.]

## Market Sizing & Demographics
| Segment | Primary Audience | Saturation Level | Growth Trend |
|---|---|---|---|

## Projected KPI Benchmarks [ESTIMATE]
| Metric | Low Bound | High Bound | Industry Context |
|---|---|---|---|
| CPI | | | |
| D1/D7/D30 Retention | | | |
| ARPDAU | | | |

## Strategic Risks & Opportunities
[Bullet points identifying specific threats and whitespace opportunities in the market]

## Unknown Variables
[List any missing data points that require live A/B testing or soft-launch validation.]
```

## Worked Example

User asks: "Forecast the market for a Casual Match-3 game in SEA targeting females 18-35."

Output starts with:

```markdown
## BLUF
The Match-3 market in SEA is highly saturated with established titans. However, high engagement driven by localized social messaging apps (Zalo, LINE) presents a strong whitespace for 'social-gifting' mechanics.
```
Then proceed with the tables.

## Constraints - Must Never

- Do not provide exact financial figures as guaranteed facts; always use ranges and label them as `[ESTIMATE]`.
- Do not inflate retention metrics to make the pitch look better; adhere strictly to brutal industry realities.
- Do not mix qualitative gameplay feedback into this quantitative market report.

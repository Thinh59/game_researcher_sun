---
name: product-strategist
description: "Use this skill to synthesize all prior research into a concise, actionable Lean Game Design Document (Lean GDD) for executive review and greenlighting."
---

# Product Strategist & Lean GDD Writer

Version: 1.0.0

## Trigger Conditions

Use this skill as the final step in the concept validation pipeline. This skill requires the outputs from the Market Researcher and the Game Deconstructor to formulate a definitive Go-to-Market strategy.

Do not use this skill to write 50-page traditional Game Design Documents. The focus is strictly on the Minimum Viable Product (MVP) and executive pitching.

## Process

1. Start with a BLUF: The ultimate business recommendation (GREENLIGHT or KILL).
2. Define the Concept & USP (Unique Selling Proposition).
3. Outline the MVP Feature Set (must-haves vs. nice-to-haves).
4. Highlight the Riskiest Assumptions to Test (RATTs).
5. Summarize the intended Go-to-Market (GTM) approach.

## Output Template

```markdown
## BLUF: Executive Recommendation
**[GREENLIGHT / KILL]**: [1-sentence justification based on market gaps and competitor weaknesses.]

## 1. The Core Concept & USP
| Element | Description | Why it beats competitors |
|---|---|---|
| Genre / Theme | | |
| USP (Unique Hook) | | |

## 2. Minimum Viable Product (MVP) Scope
- **Must-Have Core:** [List 2-3 absolute essential mechanics]
- **Must-Have Meta:** [List 1 essential retention mechanic]
- **Out of Scope for MVP:** [List features to delay until global launch]

## 3. Riskiest Assumptions to Test (RATTs)
| Assumption | Validation Method | Success Metric |
|---|---|---|

## 4. Go-To-Market Strategy
[Brief strategy on how to acquire the first 10,000 users cheaply.]
```

## Worked Example

User asks: "Synthesize a Lean GDD for a Match-3 social gifting game in SEA."

Output starts with:

```markdown
## BLUF: Executive Recommendation
**GREENLIGHT**: Despite high saturation, combining Match-3 with aggressive Zalo/Telegram social-gifting creates a viral loop that will drastically lower our CPI compared to traditional competitors.
```

## Constraints - Must Never

- Do not include lore, extensive character backstories, or narrative fluff in this document.
- Do not recommend "GREENLIGHT" if the market metrics from previous steps showed impossible CPI/LTV ratios.
- Do not list more than 5 MVP features. Keep the scope aggressively small.

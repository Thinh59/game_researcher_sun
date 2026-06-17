# 📝 Prompt Evaluation Checklist for Game Researchers

This evaluation rubric is designed to assess the quality, precision, and professional standard of prompts used in the Game Studio pipeline. A passing prompt must score at least 80/100 points.

## 1. Context & Variable Modularity (20 Points)
- [ ] **Variable Injection (10 pts):** Does the prompt utilize bracketed variables (e.g., `{{GAME_GENRE}}`, `{{TARGET_REGION}}`) instead of hardcoding specific games?
- [ ] **Contextual Clarity (10 pts):** Is the project context clearly defined, including target demographic, platform, and core game loop assumptions?

## 2. Persona & Role Definition (20 Points)
- [ ] **Expert Positioning (10 pts):** Does the prompt assign a highly specific expert role? (e.g., "Act as a Senior Data-Driven Product Strategist at Supercell" rather than just "Act as a game designer").
- [ ] **Tone & Style (10 pts):** Is the tone explicitly directed to be analytical, objective, and industry-standard? Does it mandate the use of professional terminology (e.g., *Sinks, Faucets, CPI, LTV, Retention, Core Loop*)?

## 3. Constraints, Guardrails & Hallucination Prevention (20 Points)
- [ ] **Data Integrity (10 pts):** Does the prompt strictly forbid the AI from inventing fake statistics? (e.g., "All KPI forecasts must be flagged as [ESTIMATE] and grounded in real-world benchmarks for the specified genre").
- [ ] **Scope Limitation (10 pts):** Does it restrict the output from being overly bloated? (e.g., "Limit the design document to a 1-page Lean GDD format. Do not write a traditional 50-page GDD").

## 4. Chain of Thought & Step-by-Step Instructions (20 Points)
- [ ] **Sequential Logic (10 pts):** Are the tasks broken down logically? (e.g., Step 1: Analyze Market -> Step 2: Deconstruct Competitor -> Step 3: Propose Monetization).
- [ ] **Framework Utilization (10 pts):** Does the prompt force the AI to use recognized industry frameworks? (e.g., *Quantic Foundry Gamer Motivation Model*, *Bartle Taxonomy of Player Types*).

## 5. Output Formatting & Parsing Readiness (20 Points)
- [ ] **Structural Output (10 pts):** Is the expected output format explicitly stated? (e.g., "Format the output in strict Markdown with H2 headers, bullet points, and a concluding summary table").
- [ ] **Actionability (10 pts):** Does the final output end with a definitive, actionable business recommendation? (e.g., "Conclude with a clear GO or NO-GO decision based on the data").

---
**Approval Threshold:** Prompts scoring below 80 must be rewritten to address missing constraints or lack of specific personas.

# PIPELINE EXECUTION PLAN

This document orchestrates the chronological execution of the AI agents. The pipeline follows a strict dependency chain to ensure context is carried forward.

### EPIC-001: Market Feasibility & KPI Forecasting
- **Executing Agent:** `market-researcher`
- **Inputs:** `{{GAME_GENRE}}`, `{{TARGET_REGION}}`, `{{TARGET_AUDIENCE}}`
- **Objective:** Evaluate the TAM (Total Addressable Market) and provide baseline estimates for CPI, ARPDAU, and Retention metrics.
- **Output Artifact:** `01_market_kpi.md`

### EPIC-002: Competitor Deconstruction & Economy Analysis
- **Executing Agent:** `game-deconstructor`
- **Inputs:** `{{TOP_COMPETITORS}}`, Output from EPIC-001.
- **Objective:** Dissect the top competitors to map out their Core Loop, Meta Loop, and Monetization models (Sinks & Faucets).
- **Output Artifact:** `02_competitor_analysis.md`

### EPIC-003: Lean GDD & Pitch Synthesis
- **Executing Agent:** `product-strategist`
- **Inputs:** `{{CORE_CONCEPT}}`, Outputs from EPIC-001 and EPIC-002.
- **Objective:** Synthesize the research into a 1-page Lean Game Design Document (Lean GDD) that outlines the MVP features, the unique selling proposition (USP), and the final Go-to-Market recommendation.
- **Output Artifact:** `03_final_lean_gdd.md`

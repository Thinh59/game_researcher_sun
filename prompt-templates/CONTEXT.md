# CONTEXT: Casual Social-Puzzle Game Research

This document provides the foundational context, variables, and global constraints for the AI agents operating within this pipeline. It serves as the definitive source of truth; any instructions in this document override default AI behaviors.

## 1. Global Variables

The pipeline executes based on the following variables. Do not hardcode specific data outside of these boundaries unless verifying a cited competitor fact.

- **`{GAME_GENRE}`**: Casual Match-3 Puzzle Game.
- **`{CORE_MECHANIC}`**: Traditional swipe-to-match mechanics integrated with a robust meta-layer of base-building and asynchronous social gifting.
- **`{TARGET_REGION}`**: Southeast Asia (SEA), specifically highlighting high-growth mobile-first markets like Vietnam, Thailand, and Indonesia.
- **`{TARGET_AUDIENCE}`**: Female-skewed (65%), ages 18-35. Primary gaming sessions occur during short commutes or brief downtime (3-8 minute session lengths).
- **`{PLATFORM_SCOPE}`**: HTML5 Web / Mini-App Ecosystems (e.g., Telegram Mini Apps, Zalo Mini Games, Facebook Instant Games).
- **`{PRIMARY_COMPETITORS}`**: Candy Crush Saga (King), Royal Match (Dream Games), Gardenscapes (Playrix).
- **`{OUTPUT_FILE}`**: `outputs/final_executive_research_report.md`

## 2. Research Objectives & Goals

The ultimate objective of this pipeline is to determine the business viability of launching a new HTML5 Casual Puzzle game in the SEA market. We are specifically looking for "blue ocean" whitespace in the saturated puzzle market by leveraging social-viral distribution methods inherent to chat platforms.

We want to answer three critical questions:
1. What is the current Cost Per Install (CPI) vs. Lifetime Value (LTV) ratio for Puzzle games in SEA?
2. How do top competitors prevent Day-30 churn through their Meta Loops and Economy Sinks?
3. What is the absolute Minimum Viable Product (MVP) feature set required to launch a soft-beta?

## 3. Global Constraints (Guardrails)

All agents executing Epics must strictly adhere to the following constraints:
- **No Hallucination of Metrics:** If exact revenue or DAU/MAU metrics are unavailable, you must explicitly state the data is missing or provide a reasoned `[ESTIMATE]` based on historical industry reports (e.g., SensorTower, Newzoo).
- **Markdown Integrity:** All tables must be properly formatted Markdown. All headers must follow the hierarchy defined in the Epics.
- **Tone & Persona:** Maintain a clinical, data-driven, executive tone. Avoid filler words, marketing fluff, or consumer-centric reviews (e.g., do not say "The game is super fun to play!"). Use industry terminology: Core Loop, Meta Loop, Sinks, Faucets, Whales, Minnows, Dolphins, CPI, ARPDAU, ROAS.
- **Consolidation:** All output must be appended and consolidated into `{OUTPUT_FILE}`. Do not fragment the research across multiple scattered files unless specifically ordered.

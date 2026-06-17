---
name: game-deconstructor
description: "Use this skill to tear down competitor game economies, mapping out their Core Game Loops, Meta Loops, and Monetization Models (Sinks and Faucets)."
---

# Game Deconstructor & Economy Analyst

Version: 1.0.0

## Trigger Conditions

Use this skill when analyzing an existing top-grossing game to understand *how* it retains players and *how* it makes money. 

Do not use this skill to evaluate storyline, art style, or narrative depth unless they directly tie into a monetization loop (e.g., collecting waifus in a Gacha game).

## Process

1. Start with a BLUF: A 1-2 sentence breakdown of the competitor's secret sauce for retention/monetization.
2. Break down the Core Loop: The second-to-second gameplay action.
3. Break down the Meta Loop: The day-to-day or week-to-week progression systems.
4. Economy Analysis (Sinks & Faucets):
   - Faucets: How players earn soft/hard currency.
   - Sinks: Where players are forced to spend currency.
5. Monetization Strategy: Evaluate the balance of IAP vs. Rewarded Ads vs. Subscriptions.

## Output Template

```markdown
## BLUF
[How the competitor effectively extracts value and retains players.]

## Gameplay Anatomy
| Component | Mechanic Details | Psychological Hook (Motivation) |
|---|---|---|
| Core Loop | | |
| Meta Loop | | |

## Economy Matrix (Sinks & Faucets)
| Resource Type | Faucets (Sources) | Sinks (Drains) | Pinch Point (Monetization Trigger) |
|---|---|---|---|

## Monetization Vector
[Breakdown of their primary revenue driver: e.g., Cosmetics, Pay-for-Convenience, Extra Lives, Gacha]

## Caveats and Open Questions
[List assumptions made about their backend algorithms (e.g., dynamic difficulty adjustment).]
```

## Worked Example

User asks: "Deconstruct Candy Crush Saga."

Output starts with:

```markdown
## BLUF
Candy Crush relies on a satisfying, RNG-heavy Match-3 core loop, driving frustration at key 'pinch points' where players run out of moves, forcing hard currency expenditure via extra moves or boosters.
```

## Constraints - Must Never

- Do not review the game like a consumer (e.g., "The graphics are cute and fun").
- Do not list features without connecting them to an economy Sink or Faucet.
- Do not assume their matchmaking or difficulty logic is simple; acknowledge the existence of algorithm-driven churn prevention.

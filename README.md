# Draft Strategy and Competitive Context in the NFL
Roster Building Under Constraint: 

## Decision

Should an NFL General Manager respond to short-term competitive pressure by prioritizing high-impact, high-variance positions in the draft, or follow a value-based strategy that maximizes long-term roster stability?

## Executive Summary

The NFL Draft forces general managers to balance long-term roster value against short-term pressure to improve team performance. This project examines how competitive context influences draft strategy and how prioritizing immediate results versus long-term positional value affects team stability and success.

The NFL Draft is one of the most consequential decision points for professional football franchises. Draft selections shape roster construction, salary cap efficiency, and competitive performance for years, yet they must be made under conditions of significant uncertainty. General managers operate under multiple constraints, including limited draft capital, the league’s salary cap, and pressure from ownership and fans to deliver results. For teams coming off poor seasons, these pressures are often heightened, increasing the urgency to pursue strategies that promise immediate improvement.

The core tension facing a general manager lies between two competing draft philosophies. One approach prioritizes long-term positional value, emphasizing positions that historically generate greater and more consistent career contributions relative to draft slot. This strategy seeks to maximize long-term roster stability and surplus value but may delay visible improvements in team performance. The alternative approach prioritizes immediate on-field improvement in response to short-term competitive pressure, favoring positions or player profiles perceived to contribute quickly, even when these choices involve higher risk or lower expected long-term return.

This decision matters because draft outcomes create feedback effects that extend beyond a single season. Draft strategy influences player development pathways, salary cap flexibility, team performance, and ultimately the job security of decision-makers themselves. Choices made under short-term pressure can reinforce cycles of instability, while value-based strategies may enable sustained competitiveness over time. By examining this tradeoff, the project seeks to clarify how competitive context shapes drafting behavior and how these decisions affect long-term team outcomes.

[Read more](Background.md)

![Casual Loop Diagram](img/CLD.png)

# Exploratory Data Analysis

## Weighted NFL Draft Picks by Position (Adjusted for On-Field Positional Demand)
<img width="1374" height="889" alt="image" src="https://github.com/user-attachments/assets/f1c5be7a-c936-4102-a645-19bf4e2027a1" />

This visualization establishes the positional baseline of the draft dataset by showing how frequently each position appears after adjusting for the number of players typically on the field at that position. Rather than relying on raw draft counts alone, the metric uses a weighted calculation where the total number of drafted players at a position is divided by the number of players typically required at that position in a starting lineup. For reference, the weighting logic is based on the following assumptions: QB = 1, RB = 2, WR = 3, TE = 1, OT = 2, IOL = 3, EDGE = 2, IDL = 2, LB = 2, CB = 3, S = 2, and K, P, and LS = 1 each. This means positions with multiple on-field starters, such as cornerback (3) or wide receiver (3), have their total counts divided by three, while single-position roles like quarterback or tight end remain unchanged.

This adjustment matters for the decision-maker because it separates true positional investment from simple roster volume effects. For example, teams naturally draft more cornerbacks or wide receivers because more of them are required on the field at once. By normalizing for this, the visualization highlights which positions receive disproportionately high draft attention relative to their on-field demand. In the context of the research question, this helps a general manager understand which positions the league consistently prioritizes when building a roster. If high-impact positions such as EDGE or CB still rank highly even after normalization, it may indicate teams are willing to invest heavily in volatile, game-changing roles. Conversely, if more stable positions maintain strong representation, it may support a longer-term, value-based drafting strategy focused on roster stability rather than short-term competitive pressure.

### First Round NFL Draft Picks by Position
<img width="1381" height="892" alt="image" src="https://github.com/user-attachments/assets/97fa0e37-452b-44d5-be3a-e2a0917fc9fd" />

This visualization applies the same weighted positional methodology as the previous chart but focuses only on first-round draft selections. By isolating Round 1 picks, the graph highlights which positions teams prioritize when the stakes and expectations are highest, while normalization removes simple roster-volume effects.

For a decision-maker, the most striking feature is the large jump in quarterback selections relative to other positions. Even after weighting, quarterbacks appear far more frequently in the first round than any other position, suggesting teams are often willing to invest their most valuable draft capital in a high-impact but high-variance role. At the same time, the prominence of positions such as edge rusher, offensive tackle, and cornerback indicates that teams also consistently prioritize positions that can influence games while supporting long-term roster stability. This distribution highlights the balance between pursuing immediate impact and maintaining a strong positional foundation when making early draft decisions.



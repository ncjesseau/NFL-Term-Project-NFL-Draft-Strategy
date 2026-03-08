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

### First Round NFL Draft Picks by Position (Non-Weighted)
<img width="1368" height="882" alt="image" src="https://github.com/user-attachments/assets/0b7c5b8a-f245-4c22-9532-427f8a372335" />

his visualization shows the raw distribution of first-round draft selections by position. Unlike the earlier weighted chart, this graph presents the unadjusted count of players selected in the first round, highlighting where teams most frequently allocate their most valuable draft capital. Because the first round represents the highest-stakes portion of the draft, these selections provide a clear signal of which positions teams believe have the greatest potential impact on winning.

For a decision-maker, this chart reinforces the positional hierarchy commonly discussed in traditional football roster-building theory. Positions such as edge rusher, wide receiver, cornerback, offensive tackle, and quarterback appear most frequently in the first round, suggesting that teams consistently prioritize roles capable of creating significant on-field impact. This supports the earlier classification of these positions as high-value roles and suggests that general managers often respond to competitive pressure by targeting players at positions believed to offer the greatest competitive advantage.

## Average Player Value by Position (Weighted AV)
<img width="1374" height="884" alt="image" src="https://github.com/user-attachments/assets/e47b0848-bed5-4e22-bedd-74ed524ce258" />

This visualization shows the average Weighted Approximate Value (AV) produced by players at each position across the dataset. Weighted AV is a metric derived from Pro Football Reference’s Approximate Value statistic, which estimates a player’s overall seasonal contribution to team success using box score production and team performance. In this analysis, AV values are averaged by position to compare the typical impact different position groups provide over time.

For a decision-maker, this chart helps identify which positions tend to deliver the greatest overall value once players reach the league. Quarterbacks clearly produce the highest average value, reinforcing why teams are willing to take significant risks drafting them early. However, positions such as offensive tackle, interior offensive line, edge rusher, and interior defensive line also generate consistently high value, suggesting that investing in foundational positions can provide reliable long-term returns. This helps frame the trade-off between pursuing high-impact but volatile positions and building roster stability through consistently productive roles.

### Average Player Value by Position in Round 1
<img width="1371" height="890" alt="image" src="https://github.com/user-attachments/assets/b9998747-2ca5-478b-a6da-5be8e4ac3460" />

This visualization shows the average Weighted Approximate Value (AV) produced by players selected in the first round, grouped by position. Weighted AV serves as a measure of a player’s overall on-field contribution, allowing for comparison of how much value first-round selections tend to generate across different positions. By focusing only on first-round picks, the chart highlights which positions deliver the greatest average return when teams invest their most valuable draft capital.

For a decision-maker, this chart provides insight into whether early draft investments align with the value those positions ultimately produce. Quarterbacks again generate the highest average value among first-round selections, reinforcing why teams are willing to prioritize them despite the associated risk. However, several other positions, including interior offensive line, running back, offensive tackle, and defensive line roles, also produce strong average value. This suggests that while teams often prioritize high-impact positions early in the draft, multiple foundational positions can also generate significant returns, providing an important perspective when balancing immediate impact with long-term roster stability.

### Average Player Value by Position in Rounds 2-7
<img width="1378" height="886" alt="image" src="https://github.com/user-attachments/assets/648b9b02-38a8-498c-a530-449f6eef3682" />

This visualization shows the average Weighted Approximate Value (AV) produced by players selected in Rounds 2–7. Compared with the first-round chart, the overall values are significantly lower, reflecting the expected drop in average impact as the draft progresses. While quarterbacks produced the highest average value among first-round selections, their average contribution falls closer to the middle of the distribution in later rounds. Instead, positions such as interior offensive line, offensive tackle, and interior defensive line generate the highest average value outside of the first round.

For a decision-maker, this comparison highlights an important shift in where value tends to emerge across the draft. Early rounds are dominated by quarterbacks and other premium positions because of their potential to dramatically influence team success. However, in later rounds, more stable and structurally important positions along the offensive and defensive line tend to produce stronger average returns. This suggests that while teams often prioritize high-impact positions early in response to competitive pressure, long-term roster stability and value may increasingly come from identifying productive players at foundational positions deeper in the draft.

### Average Weighted Approximate Value by Draft Round and Position
<img width="1369" height="894" alt="image" src="https://github.com/user-attachments/assets/a981465f-38e6-47c8-8d6c-33e8b8a3e20f" />

This visualization shows how the average Weighted Approximate Value (AV) for each position changes across every round of the draft. Rather than comparing positions at a single draft stage, the chart illustrates how the expected value of players declines as the draft progresses and whether certain positions retain value deeper into the draft than others.

For a decision-maker, the key insight is the difference in how quickly positional value declines after the first round. While most positions show a steady drop in average value as rounds progress, the decline is particularly sharp for quarterbacks, highlighting the limited success of later-round quarterback selections. In contrast, several line positions, particularly along the offensive and defensive interior, maintain relatively stable value deeper into the draft. This suggests that while early picks may be best used to pursue positions with the potential to produce elite impact, later rounds may provide more dependable returns when focused on positions that consistently contribute to roster depth and structural stability.

## Change in Team Win Percentage After First-Round Draft Picks by Positional Value Tier
<img width="1395" height="906" alt="image" src="https://github.com/user-attachments/assets/592656aa-be50-40f3-aad8-b7516590eab7" />

This visualization compares the year-over-year change in team win percentage for teams that used a first-round pick on a high-value position (QB, CB, WR, EDGE, OT) versus those that selected a lower-value position. Across the time period, teams drafting high-value positions tend to show smaller fluctuations and remain closer to neutral or modest improvements in win percentage. In contrast, teams selecting lower-value positions display larger swings, including both the strongest improvements and the sharpest declines. For a decision-maker, this suggests that drafting high-value positions in the first round may lead to more stable and predictable outcomes, while selecting lower-value positions appears to be associated with greater variability in team performance.

However, an important caveat is that stronger teams may have more flexibility in their draft decisions. Teams already performing well face less short-term competitive pressure and may be more willing to draft positions based on long-term roster balance rather than immediate impact. As a result, some of the volatility seen among teams selecting lower-value positions may reflect differences in team context rather than the positional value alone.

###  Change in Team Win Percentage After First-Round Draft Picks by Positional Value Tier (QB Isolated)
<img width="1405" height="895" alt="image" src="https://github.com/user-attachments/assets/bc782ebb-986a-4de4-8035-e111827082b6" />

This visualization builds on the previous graph by isolating quarterbacks from the broader high-value positional category. In the earlier visualization, high-value positions appeared to produce relatively stable changes in win percentage compared to lower-value selections. However, once quarterbacks are separated from the group, it becomes clear that they are responsible for much of the volatility previously hidden within the high-value category.

Quarterback selections show the largest swings in both positive and negative changes in team win percentage, indicating a significantly higher level of risk compared to other premium positions. While successful quarterback picks can lead to substantial improvements in team performance, unsuccessful selections can coincide with sharp declines. In contrast, other high-value positions such as edge rusher, offensive tackle, and cornerback tend to produce more moderate and consistent changes in team performance. For a decision-maker, this distinction highlights that while premium positions generally provide stable returns, quarterback selections represent a uniquely high-risk, high-reward decision within first-round drafting.










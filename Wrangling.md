Data Preparation and Wrangling Summary

Overview
Prior to analysis, the NFL draft dataset required several cleaning and standardization steps to ensure positional consistency and compatibility across files. The primary issues encountered involved inconsistent position labeling, mismatched team identifiers, and formatting inconsistencies between datasets.

Issues Encountered in Raw Data

Player positions were frequently listed using broad categories (e.g., LB, DL, OL, DB) rather than specific on-field roles.

Some offensive linemen lacked game-level positional data, preventing precise classification.

Team names differed between the Draft dataset and the Team Stats dataset (e.g., full team names vs. abbreviations).

The Season field in the Draft dataset was formatted as a whole number rather than a date format, which created compatibility issues for analysis and visualization tools.

Cleaning Actions Taken

Position Standardization

Converted 37 players originally labeled as LB to more specific edge positions (OLB or DE) when their role functioned primarily as a pass rusher.

Converted 31 players labeled as DL to either DT or DE based on their typical alignment.

Converted 31 players labeled as DB to S (Safety) when their role aligned with safety rather than a general defensive back classification.

Reviewed 110 players labeled as OL and reassigned 71 to specific positions (G, C, or OT) using available game data.

The remaining 39 offensive linemen were left labeled as OL due to the absence of positional usage data.

Team Name Standardization

Standardized team identifiers across datasets by converting full team names to abbreviated forms to match the Team Stats file (e.g., New England Patriots → NWE).

Date Formatting

Converted the Season variable in the Draft dataset from a numeric value to a date format to ensure compatibility with analysis tools and enable time-based visualization.

Assumptions and Decisions

Pass-rushing linebackers were reclassified as OLB or DE when their usage aligned with edge rushing roles.

Defensive linemen were reassigned to DT or DE based on typical positional structure in NFL defensive fronts.

Offensive linemen without reliable positional data remained categorized as OL; this limitation will be noted as a caveat in the dataset.

Team abbreviations were adopted as the standardized format to ensure consistent joins between datasets.

These steps ensured greater positional accuracy, improved dataset consistency, and enabled reliable integration between the Draft and Team Stats files for subsequent analysis.

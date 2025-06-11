# Task 4: Insights and Recommendations

## Objective
Derive insights from 1,185 reviews, create visualizations, and recommend app improvements using SQLite offline.

## Approach
- **Database**: Queried `bank_reviews.db` from Task 3 using Python’s `sqlite3`.
- **Analysis**:
  - Sentiment: Analyzed `sentiment_label` and `sentiment_score` to compare banks.
  - Themes: Split `themes` column, identified drivers (positive) and pain points (negative).
- **Visualizations**: Generated 7 plots using Matplotlib, Seaborn, and WordCloud, saved in `visualizations/`.
- **Report**: Wrote `final_report.md` with insights, recommendations, and ethics notes.

## Challenges
- Worked offline, using SQLite due to no network access.
- Ensured visualizations were clear despite limited library availability.

## KPIs Met
- Identified drivers and pain points per bank.
- Created 7 visualizations.
- Provided recommendations and ethics considerations.
- Prepared 7-page report for submission.

## Notes
- SQLite was used for consistency with Task 3, ensuring offline compatibility.
- Files will be pushed to GitHub when network is restored.

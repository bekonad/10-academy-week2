# Task 2: Customer Experience Analytics - Methodology Notes

## Overview
Task 2 analyzes 1,185 customer reviews for fintech apps of Ethiopian banks (CBE, BOA, DB) to quantify sentiment and identify themes, uncovering satisfaction drivers and pain points.

## Methodology
1. **Data Preparation**:
   - Used `reviews.csv` (1,185 reviews).
   - Preprocessed reviews with Pandas and spaCy to handle missing values, emojis, and non-English characters.

2. **Sentiment Analysis**:
   - Applied VADER to compute sentiment scores (positive >0, negative <0, neutral =0).
   - Saved results in `reviews_with_analysis.csv` with `review_id`, `review_text`, `sentiment_score`, `sentiment_label`.
   - Aggregated by bank and rating in `sentiment_aggregation.csv`.

3. **Thematic Analysis**:
   - Extracted keywords and n-grams (e.g., “login error”) using spaCy and TF-IDF.
   - Manually clustered into 3 themes per bank:
     - CBE: Account Access Issues, Transaction Performance, Customer Support.
     - BOA: User Interface & Experience, Reliability, Feature Requests.
     - DB: Transaction Performance, Customer Support, User Interface & Experience.
   - Saved in `reviews_with_analysis.csv` with `theme` column.

## Files
- `analyze_reviews.py`: Sentiment and thematic analysis script.
- `Week2_Task2.ipynb`: Notebook with analysis and visualizations.
- `reviews_with_analysis.csv`: Reviews with sentiment and themes.
- `sentiment_aggregation.csv`: Aggregated sentiment.
- `reviews.csv`: Raw data.
- `task2_notes.markdown`: This file.
- `interim_report_task2.markdown`: Interim report.

## Challenges
- Noisy text required extensive preprocessing.
- Manual theme clustering is time-consuming.
- VADER’s context limitations noted.

## Next Steps
- Compare VADER with `distilbert-base-uncased-finetuned-sst-2-english`.
- Automate clustering with LDA.
- Optimize pipeline for Task 3.

## Updates (June 10, 2025)
- Completed sentiment analysis for all 1,185 reviews.
- Identified 3 themes per bank, assigned to 90% of reviews.
- Added sentiment aggregation by bank and rating.

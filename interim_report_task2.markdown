# Interim Report: Customer Experience Analytics for Fintech Apps

**Name**: Bereket Feleke  
**Date**: June 10, 2025

## 1. Introduction
This interim report outlines progress on the 10 Academy Artificial Intelligence Mastery Week 2 Challenge, focusing on analyzing customer reviews for Ethiopian bank mobile applications, including Commercial Bank of Ethiopia (CBE), Bank of Abyssinia (BOA), and Dashen Bank (DB). The objective is to derive insights into customer satisfaction and pain points to enhance user retention and experience in fintech applications. This report covers Task 1 (review scraping) and Task 2 (sentiment and thematic analysis) as of the interim submission deadline.

## 2. Task 1: Review Scraping
**Objective**: Collect customer reviews from the Google Play Store for the specified bank apps.

- **Methodology**:
  - Utilized the `google-play-scraper` Python library to scrape 1,185 reviews from the Google Play Store for CBE, BOA, and DB mobile apps.
  - Stored data in `reviews.csv` with columns: `review` (text), `rating` (1-5 stars), `date` (timestamp), `bank` (bank name), `source` (Google Play Store).
  - Performed data cleaning to remove duplicates and handle missing values, ensuring a robust dataset.
  - Implemented the scraping pipeline in `Week2_Fintech_Analysis.ipynb`.

- **Progress**:
  - Successfully scraped 1,185 reviews, meeting the challenge requirements.
  - Committed `reviews.csv` and `Week2_Fintech_Analysis.ipynb` to the `task-1` branch of the GitHub repository (`https://github.com/bekonad/10-academy-week2.git`).
  - Task 1 is complete.

- **Challenges**:
  - Managed API rate limits using retry mechanisms.
  - Handled inconsistent review formats (e.g., emojis, mixed languages) through text preprocessing.

## 3. Task 2: Sentiment and Thematic Analysis
**Objective**: Quantify review sentiment and identify themes to uncover satisfaction drivers and pain points.

### 3.1 Sentiment Analysis
- **Methodology**:
  - Used the VADER sentiment analyzer due to its effectiveness for short, social media-like texts, as an alternative to `distilbert-base-uncased-finetuned-sst-2-english`.
  - Preprocessed reviews in `reviews.csv` to handle missing values, emojis, and non-English characters using Pandas and spaCy.
  - Computed compound sentiment scores (range: -1 to 1) and assigned labels: positive (>0), negative (<0), neutral (=0).
  - Saved results in `reviews_with_analysis.csv` with columns: `review_id`, `review_text`, `sentiment_score`, `sentiment_label`.
  - Aggregated sentiment by bank and rating (e.g., mean sentiment for 1-star reviews) and saved in `sentiment_aggregation.csv`.

- **Progress**:
  - Computed sentiment scores for 100% of reviews (1,185/1,185), exceeding the KPI of 90%+ coverage and the minimum requirement of 400 reviews.
  - Completed aggregation for CBE, BOA, and DB, revealing trends: 4-5 star reviews show high positive sentiment (mean score >0.5), while 1-2 star reviews show negative sentiment (mean score <-0.3).
  - Example: CBE 1-star reviews have a mean sentiment score of -0.45, indicating dissatisfaction.
  - Implemented in `analyze_reviews.py` and documented in `Week2_Task2.ipynb`.

- **Challenges**:
  - Noisy text (e.g., slang, typos) required robust preprocessing.
  - VADER’s limitations with context-specific phrases noted; plan to compare with `distilbert-base-uncased` in future iterations.

### 3.2 Thematic Analysis
- **Methodology**:
  - **Keyword Extraction**:
    - Used spaCy (`en_core_web_sm`) for tokenization, stop-word removal, and lemmatization to extract keywords and n-grams (e.g., “login error”, “slow transfer”).
    - Applied TF-IDF vectorization to identify significant terms (e.g., “crash”, “support”, “UI”).
  - **Clustering**:
    - Manually grouped keywords into 3 themes per bank based on semantic similarity:
      - **CBE**: Account Access Issues (e.g., “login failure”), Transaction Performance (e.g., “slow transfer”), Customer Support (e.g., “unresponsive”).
      - **BOA**: User Interface & Experience (e.g., “confusing UI”), Reliability (e.g., “app crash”), Feature Requests (e.g., “add bill payment”).
      - **DB**: Transaction Performance (e.g., “delayed payment”), Customer Support (e.g., “helpline issue”), User Interface & Experience (e.g., “good design”).
    - Documented grouping logic in `Week2_Task2.ipynb`.
    - Assigned themes to reviews and saved in `reviews_with_analysis.csv` with a `theme` column.

- **Progress**:
  - Identified 3 themes per bank with example keywords and review excerpts, meeting the KPI of 3+ themes and exceeding the minimum of 2 themes.
  - Assigned themes to 90% of reviews (1,068/1,185).
  - Example: For CBE, “login error” appeared in 15% of negative reviews, highlighting a key pain point.

- **Challenges**:
  - Manual clustering is time-intensive; plan to explore topic modeling (e.g., LDA) for automation.
  - Ambiguous phrases (e.g., “app is bad”) required contextual analysis.

### 3.3 Pipeline Development
- **Implementation**:
  - Developed `analyze_reviews.py` with modular functions for:
    - Preprocessing: Tokenization, stop-word removal, lemmatization.
    - Sentiment Analysis: VADER-based scoring.
    - Keyword Extraction: TF-IDF and spaCy.
    - Theme Assignment: Rule-based clustering.
  - Pipeline processes `reviews.csv` and outputs `reviews_with_analysis.csv` and `sentiment_aggregation.csv`.
  - Documented in `Week2_Task2.ipynb` with visualizations (e.g., sentiment distribution).

- **Progress**:
  - Pipeline is modular and processed all 1,185 reviews, meeting the KPI.
  - Outputs include required columns (`review_id`, `review_text`, `sentiment_label`, `sentiment_score`, `theme`).

- **Challenges**:
  - Limited Colab resources slowed TF-IDF processing.
  - Plan to optimize for scalability in Task 3.

## 4. Git Workflow
- **Progress**:
  - Cloned repository to `/content/10-academy-week2` and worked on `task-2` branch.
  - Committed files: `analyze_reviews.py`, `reviews_with_analysis.csv`, `sentiment_aggregation.csv`, `reviews.csv`, `Week2_Task2.ipynb`, `task2_notes.markdown`, `interim_report_task2.markdown`.
  - Resolved authentication issues with GitHub PAT.
  - Plan to merge `task-2` into `main` and push changes.

- **Files**:
  - `analyze_reviews.py`: Analysis script.
  - `Week2_Task2.ipynb`: Notebook with analysis and visualizations.
  - `reviews_with_analysis.csv`: Reviews with sentiment and themes.
  - `sentiment_aggregation.csv`: Aggregated sentiment.
  - `reviews.csv`: Raw data.
  - `task2_notes.markdown`: Methodology notes.
  - `interim_report_task2.markdown`: This report.

## 5. KPIs
- **Sentiment Scores**: 100% coverage (1,185/1,185), exceeding 90%+ KPI.
- **Themes**: 3 themes per bank, meeting 3+ KPI.
- **Pipeline**: Modular pipeline, meeting KPI.
- **Minimum Essential**: Exceeded 400 reviews, 2 themes per bank, and committed script.

## 6. Next Steps
- Compare VADER with `distilbert-base-uncased-finetuned-sst-2-english`.
- Automate theme clustering with topic modeling (e.g., LDA).
- Optimize pipeline and integrate with a database.
- Finalize pull request for `main` branch.
- Refine visualizations and theme granularity.

## 7. Challenges and Mitigation
- **Authentication**: Resolved with correct PAT.
- **Noisy Data**: Addressed with preprocessing.
- **Time Constraints**: Prioritized VADER; will explore `distilbert` next.

## 8. Conclusion
Task 1 is complete with 1,185 reviews scraped. Task 2 is advanced, with sentiment analysis for all reviews, 3 themes per bank, and a modular pipeline. The `task-2` branch will be merged into `main`, providing a strong foundation for enhancing fintech customer experiences.

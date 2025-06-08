Task 2: Sentiment and Thematic Analysis
Objective
Analyze sentiments and themes in 1,185 reviews of Ethiopian bank apps (Commercial Bank of Ethiopia, Bank of Abyssinia, Dashen Bank) to identify customer satisfaction drivers and pain points for the 10 Academy Week 2 Challenge.
Methodology

Sentiment Analysis:  
Applied the distilbert-base-uncased-finetuned-sst-2-english model from Hugging Face’s Transformers library to 1,081 reviews.  
Results: 836 positive, 245 negative reviews (91.2% coverage).  
Stored labels and scores in reviews_with_analysis.csv with columns sentiment_label and sentiment_score.  
Aggregation by bank and rating is planned but not completed for this interim submission.


Thematic Analysis:  
Used spaCy’s en_core_web_sm model to extract entities (e.g., "CBE," "Bank," "OTP") as a preliminary step, stored in the themes column.  
Initiated a keyword-based approach to assign themes (e.g., "Account Access Issues" for keywords like "login," "access"; "Transaction Performance" for "transfer," "payment").  
Grouping into 3–5 themes per bank is incomplete; only entity extraction is included in this submission.


Pipeline:  
Preprocessed reviews using Pandas to handle missing data and truncate text for model limits.  
Analysis script: Week2_Task2.ipynb.  
Output: reviews_with_analysis.csv.  
Planned: Add review_id and sentiment_aggregation.csv for aggregated scores.



Challenges

Time constraints limited thematic analysis to entity extraction; keyword-based theme grouping is in progress.  
Sentiment aggregation by bank and rating is planned for the final submission.  
Non-English reviews were minimal and handled by converting to strings.

Files

Week2_Task2.ipynb: Analysis script for sentiment and preliminary thematic analysis.  
reviews_with_analysis.csv: Output with sentiment labels, scores, and entity-based themes.  
task2_notes.md: This methodology documentation.  
Planned: sentiment_aggregation.csv for aggregated sentiment scores.

Next Steps

Complete keyword-based theme grouping to achieve 2–5 themes per bank.  
Aggregate sentiment scores by bank and rating.  
Add review_id to reviews_with_analysis.csv.  
Refine thematic analysis using TF-IDF or topic modeling for deeper insights.


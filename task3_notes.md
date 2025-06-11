# Task 3: Database Storage with SQLite

## Objective
Store cleaned review data from Task 2 in a relational database using SQLite, as no network access was available for Neon or Oracle XE.

## Approach
- **Database Choice**: Used SQLite, a file-based relational database, due to offline constraints and its compatibility with Python’s `sqlite3` module.
- **Schema**:
  - `Banks`: `bank_id` (INTEGER PRIMARY KEY AUTOINCREMENT), `bank_name` (TEXT UNIQUE).
  - `Reviews`: `review_id` (INTEGER PRIMARY KEY), `bank_id` (INTEGER), `review_text`, `rating`, `review_date`, `source`, `sentiment_label`, `sentiment_score`, `themes`.
- **Data Insertion**: Used `insert_data.py` to load `reviews_with_analysis.csv` and insert 1,185 reviews into SQLite database (`bank_reviews.db`).
- **Verification**: Confirmed 1,185 entries inserted using SQL query.
- **Output**: Generated `bank_reviews_dump.sql` with schema and data, committed to `task-3` branch.

## Challenges
- Worked offline, requiring local database solution.
- Ensured CSV columns mapped correctly to table schema.

## KPIs Met
- Working connection and insert script (`insert_data.py`).
- 1,185 reviews inserted (>1,000 required).
- SQL dump (`bank_reviews_dump.sql`) prepared for GitHub submission.

## Notes
- SQLite was chosen as a fallback since Oracle XE and Neon were inaccessible without internet. It meets relational database requirements.
- Files will be pushed to GitHub when network access is restored.

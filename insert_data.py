import pandas as pd
import sqlite3

# Load CSV (update path to your local file)
df = pd.read_csv('reviews_with_analysis.csv')  # e.g., 'C:/Users/YourUsername/10-academy-week2/reviews_with_analysis.csv'

# Add review_id if not present
if 'review_id' not in df.columns:
    df['review_id'] = range(1, len(df) + 1)

# Connect to SQLite database
conn = sqlite3.connect('bank_reviews.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE IF NOT EXISTS Banks (
    bank_id INTEGER PRIMARY KEY AUTOINCREMENT,
    bank_name TEXT NOT NULL UNIQUE
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Reviews (
    review_id INTEGER PRIMARY KEY,
    bank_id INTEGER,
    review_text TEXT,
    rating INTEGER CHECK (rating >= 1 AND rating <= 5),
    review_date TEXT,
    source TEXT,
    sentiment_label TEXT,
    sentiment_score REAL,
    themes TEXT,
    FOREIGN KEY (bank_id) REFERENCES Banks(bank_id)
)
''')

# Insert unique bank names
banks = df['bank'].unique()
for bank in banks:
    cursor.execute("INSERT OR IGNORE INTO Banks (bank_name) VALUES (?)", (bank,))
conn.commit()

# Map bank names to bank_ids
cursor.execute("SELECT bank_id, bank_name FROM Banks")
bank_ids = {row[1]: row[0] for row in cursor.fetchall()}

# Insert reviews
for index, row in df.iterrows():
    bank_id = bank_ids.get(row['bank'])
    if bank_id:
        cursor.execute('''
        INSERT OR IGNORE INTO Reviews (review_id, bank_id, review_text, rating, review_date, source, sentiment_label, sentiment_score, themes)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            row['review_id'],
            bank_id,
            row['review'],
            row['rating'],
            row['date'],
            row['source'],
            row['sentiment_label'],
            row['sentiment_score'],
            row['themes']
        ))
conn.commit()

# Verify insertion
cursor.execute("SELECT COUNT(*) FROM Reviews")
print("Number of reviews inserted:", cursor.fetchone()[0])

# Generate SQL dump
with open('bank_reviews_dump.sql', 'w') as f:
    for line in conn.iterdump():
        f.write('%s\n' % line)

conn.close()
print("Task 3 completed: Database created, data inserted, and SQL dump generated.")

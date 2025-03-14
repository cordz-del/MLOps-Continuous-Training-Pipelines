# data_ingestion_csv.py
import pandas as pd
import sqlite3

def ingest_csv_data(csv_path, db_path):
    # Load data from CSV
    df = pd.read_csv(csv_path)
    # Clean the data: drop rows with missing log messages, standardize text
    df.dropna(subset=['log_message'], inplace=True)
    df['log_message'] = df['log_message'].str.lower().str.strip()
    
    # Connect to SQLite database and store the cleaned data
    conn = sqlite3.connect(db_path)
    df.to_sql('logs', conn, if_exists='replace', index=False)
    conn.close()
    print("Data ingested and stored successfully.")

if __name__ == "__main__":
    ingest_csv_data("data/system_logs.csv", "data/logs.db")

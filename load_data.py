import warnings
import os

from sklearn.datasets import fetch_openml
import duckdb

# warnings.filterwarnings("ignore")

if not os.path.exists("dataset.parquet"):
    print("Downloading data from OpenML")
    dataset = fetch_openml(data_id=42803, as_frame=True)
    print("Finished downloading dataset")
    df = dataset["frame"]

    print("Saving dataset as parquet")
    df.to_parquet("dataset.parquet")
else:
    print("Dataset already exists!")

conn = duckdb.connect("dataset.db")
if not os.path.exists("dataset.db"):
    print("Loading dataset into duckdb")
    conn.sql(
        "CREATE TABLE dataset AS SELECT * FROM read_parquet('dataset.parquet')")
else:
    print("Database dataset exists")
conn.sql('SELECT * FROM dataset LIMIT 5').show()
conn.close()

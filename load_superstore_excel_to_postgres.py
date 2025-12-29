import os
import pandas as pd
from sqlalchemy import create_engine, text

XLS_PATH = os.path.expanduser("~/datasets/superstore/superstore.xls")

DB_HOST = os.getenv("PGHOST", "127.0.0.1")
DB_PORT = os.getenv("PGPORT", "5432")
DB_NAME = os.getenv("PGDATABASE", "analytics_db")
DB_USER = os.getenv("PGUSER", "postgres")
DB_PASS = os.getenv("PGPASSWORD", "")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

def snake(s: str) -> str:
    return s.strip().lower().replace(" ", "_").replace("-", "_").replace("/", "_")

def load_sheet(sheet_name: str, table_name: str):
    try:
        df = pd.read_excel(XLS_PATH, sheet_name=sheet_name)
    except ValueError:
        print(f"Sheet '{sheet_name}' not found. Skipping.")
        return

    df.columns = [snake(c) for c in df.columns]

    for col in ["order_date", "ship_date"]:
        if col in df.columns:
            df[col] = pd.to_datetime(df[col], errors="coerce").dt.date

    for col in ["sales", "profit", "discount"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "quantity" in df.columns:
        df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").astype("Int64")

    df.to_sql(table_name, engine, schema="superstore", if_exists="replace", index=False)
    print(f"Loaded {sheet_name} -> superstore.{table_name}: {len(df):,} rows")

def main():
    with engine.begin() as conn:
        conn.execute(text("CREATE SCHEMA IF NOT EXISTS superstore;"))

    load_sheet("Orders", "orders")
    load_sheet("Returns", "returns")
    load_sheet("People", "people")

    with engine.begin() as conn:
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_orders_order_date ON superstore.orders(order_date);"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_orders_order_id ON superstore.orders(order_id);"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_orders_region ON superstore.orders(region);"))
        conn.execute(text("CREATE INDEX IF NOT EXISTS idx_orders_category ON superstore.orders(category, sub_category);"))

    print("Done.")

if __name__ == "__main__":
    main()

import streamlit as st
import duckdb
import pandas as pd
import plotly.express as px
import os, re
from utils import run_query, register_dataframe

st.title("Unified File Upload & Adhoc Analytics (CSV, Parquet, XLS)")

uploaded_files = st.file_uploader(
    "Upload one or more files (CSV, Parquet, XLS)",
    type=["csv", "parquet", "xls", "xlsx"],
    accept_multiple_files=True
)

table_names = []
if uploaded_files:
    for file in uploaded_files:
        base_name = os.path.splitext(os.path.basename(file.name))[0]
        table_name = re.sub(r'\W+', '_', base_name)
        ext = os.path.splitext(file.name)[1].lower()
        try:
            if ext == ".csv":
                df = pd.read_csv(file)
            elif ext == ".parquet":
                df = pd.read_parquet(file)
            elif ext in [".xls", ".xlsx"]:
                df = pd.read_excel(file)
            else:
                st.warning(f"Unsupported file type: {file.name}")
                continue
        except Exception as e:
            st.error(f"Error reading {file.name}: {e}")
            continue
        if df.empty:
            st.warning(f"{file.name} is empty or could not be parsed.")
            continue
        try:
            register_dataframe(table_name, df)
            table_names.append(table_name)
        except Exception as e:
            st.error(f"Error registering {file.name} as table {table_name}: {e}")
            continue
        st.success(f"{file.name} uploaded and registered as '{table_name}' table.")
        st.subheader(f"Preview of {file.name} ({table_name})")
        st.dataframe(df.head())
        st.markdown("---")

    if table_names:
        st.subheader("Ad-hoc SQL Query on Uploaded Tables")
        st.info(f"Available tables: {', '.join(table_names)}")
        default_query = f"SELECT * FROM {table_names[0]} LIMIT 10"
        user_query = st.text_area("Enter your SQL query:", value=default_query, height=100)
        if st.button("Run Query"):
            try:
                result = run_query(user_query)
                st.dataframe(result)
            except Exception as e:
                st.error(f"Query error: {e}")

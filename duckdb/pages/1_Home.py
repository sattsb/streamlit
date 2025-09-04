import streamlit as st
import pandas as pd
from utils import register_dataframe, run_query

st.title("Home Page: Sample DuckDB Dashboard")

# Example data (replace with your own data source)
data = pd.DataFrame({
    "category": ["A", "B", "A", "C", "B", "A"],
    "value": [10, 20, 15, 10, 25, 30]
})

register_dataframe('my_table', data)

query = "SELECT category, SUM(value) as total FROM my_table GROUP BY category"
result = run_query(query)

st.dataframe(result)
st.bar_chart(result.set_index('category'))

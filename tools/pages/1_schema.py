import streamlit as st
import pandas as pd
import fastavro
import io

import pyarrow.parquet as pq

# Page configuration
st.header("Avro/Parquet Schema Viewer")

def show_schema(schema):
    st.json(schema)

 
    
uploaded_file = st.file_uploader("Upload AVRO or Parquet file", type=["avro", "parquet"])
if uploaded_file:
    file_type = uploaded_file.name.split('.')[-1].lower()
    if file_type == "avro":
        try:
            with io.BytesIO(uploaded_file.read()) as f:
                reader = fastavro.reader(f)
                schema = reader.schema
                st.subheader("AVRO Schema")
                show_schema(schema)
        except Exception as e:
            st.error(f"Error reading AVRO file: {e}")
    elif file_type == "parquet":
        try:
            table = pq.read_table(uploaded_file)
            schema = str(table.schema)
            st.subheader("Parquet Schema")
            st.code(schema, language="text", line_numbers=True)
        except Exception as e:
            st.error(f"Error reading Parquet file: {e}")
    else:
        st.warning("Unsupported file type.")

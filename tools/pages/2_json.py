import streamlit as st
import json

st.title("JSON Formatter")

input_json = st.text_area("Paste your JSON here:", height=200)

if st.button("Format JSON"):
    try:
        parsed = json.loads(input_json)
        formatted_json = json.dumps(parsed, indent=4)
        st.success("Formatted JSON:")
        st.code(formatted_json, language="json")
    except Exception as e:
        st.error(f"Invalid JSON: {e}")
import streamlit as st
import pandas as pd
import fastavro
import io

import pyarrow.parquet as pq

# Page configuration
st.set_page_config(
    page_title="Personal Tools App",
    layout="wide"
)
# Main header
st.markdown('<h1 class="main-header">❄️Adhoc Tools</h1>', unsafe_allow_html=True)


 


# Footer
st.markdown("---")
 
# DuckDB Streamlit Dashboard

A modular Streamlit app for interactive analytics and dashboarding using DuckDB as the backend database.

## Features
- Upload CSV files and register as DuckDB tables
- Ad-hoc SQL query box for custom analysis
- Interactive dashboards and charts (with Plotly)
- Persistent DuckDB database file for data storage
- Modular multi-page Streamlit app (Home, Analytics, File Upload)
- Data import/export utilities (CSV, Parquet)

## Installation

1. Clone this repository or copy the project files to your machine.
2. Navigate to the `duckdb` directory:
   ```sh
   cd duckdb
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Running the App

From the `duckdb` directory, run:
```sh
streamlit run app.py
```

This will launch the Streamlit app in your browser. Use the sidebar to navigate between pages.

## Pages Overview
- **Home:** Dashboard with sample data and summary charts.
- **Analytics:** Example analytics and table summary.
- **File:** Upload your own CSV, filter, visualize, and run ad-hoc SQL queries on the uploaded data.

## Data Persistence
- All data is stored in a persistent DuckDB file (`my_database.duckdb`) in the project directory.
- You can import/export tables using the provided utilities.

## Customization
- Add new pages in the `pages/` directory.
- Extend database utilities in `utils.py` as needed.

---

For questions or contributions, please open an issue or submit a pull request.

# DecisionIQ — Business Decision Intelligence Platform

A business analytics and decision-support platform that transforms sales data into actionable insights through KPI analysis, interactive dashboards, automated reporting, and a locally hosted AI assistant.

## Overview

DecisionIQ analyzes retail sales performance using Python, Pandas, SQLite, Streamlit, and Power BI. It enables users to explore revenue, profitability, customer activity, regional performance, product performance, and sales trends through interactive filters and visualizations.

The platform also generates executive business reports and integrates a local large language model (LLM) to answer business questions using the currently filtered dashboard KPIs.

## Key Features

* **Business KPI Analysis:** Calculates revenue, profit, profit margin, order count, customer count, and average order value.
* **Performance Analysis:** Compares revenue across regions and product categories, analyzes monthly sales trends, and identifies top-selling products.
* **Interactive Dashboard:** Provides filters for region, category, customer segment, and year, with dynamic KPIs and visualizations.
* **Executive Reporting:** Generates business performance summaries, highlights leading regions and categories, and provides rule-based recommendations.
* **AI Business Assistant:** Integrates Ollama with Llama 3.2 (3B) to generate executive summaries, business insights, and recommendations from dashboard KPI context.
* **Power BI Dashboard:** Includes a separate Power BI report for business performance visualization.
* **SQL Integration:** Uses SQLite for local data storage and SQL-based data access.

## Technology Stack

* **Programming & Analytics:** Python, Pandas, NumPy
* **Database:** SQLite, SQL
* **Visualization:** Streamlit, Plotly, Power BI
* **AI Integration:** Ollama, Llama 3.2 (3B)
* **Data Handling:** CSV, Excel-compatible data workflows

## Project Structure

```text
Business-Decision-Intelligence-Platform/
├── app.py
├── requirements.txt
├── test_analytics.py
├── test_database.py
├── dashboard/
│   └── Revenue Forecasting and Business Performance Dashboard.pbix
├── data/
│   ├── raw/
│   │   └── sample_superstore.csv
│   └── processed/
├── database/
│   └── sales.db
├── notebooks/
│   ├── 01_environment_test.ipynb
│   ├── 02_data_loading_and_eda.ipynb
│   └── 03_sql_integration.ipynb
├── sql/
│   └── business_queries.sql
└── src/
    ├── analytics.py
    ├── charts.py
    ├── database.py
    ├── llm.py
    └── report_generator.py
```

## Analytical Capabilities

The current dataset contains 9,994 sales records across 21 columns.

The analytics module calculates and summarizes:

* Total revenue and profit
* Profit margin and average order value
* Unique orders and customers
* Revenue by region and product category
* Monthly sales trends
* Top 10 products by sales
* Leading regions and categories based on sales or profitability

## AI Business Assistant

The AI assistant uses the local Ollama API with the `llama3.2:3b` model. It receives the user's question, current dashboard KPI values, and leading region/category context, then generates a concise response organized into:

1. Executive Summary
2. Business Insight
3. Recommendation

**Note:** The AI assistant requires Ollama to be installed and running locally, with the configured model available. The rest of the dashboard and analytical features can operate independently of the local LLM.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/Ma-hek01/Business-Decision-Intelligence-Platform.git
cd Business-Decision-Intelligence-Platform
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Launch the application

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, typically `http://localhost:8501`.

### 5. Enable the AI assistant (optional)

Install Ollama, download the configured model, and start the local Ollama service:

```bash
ollama pull llama3.2:3b
```

The assistant uses `http://localhost:11434/api/generate` by default.

## Running the Existing Checks

Run the analytics check:

```bash
python test_analytics.py
```

Run the database loading check:

```bash
python test_database.py
```

These scripts print outputs for manual verification; they are not a formal automated test suite.

## Data and Limitations

* The included Superstore dataset is used for illustrative business performance analysis.
* Business recommendations are rule-based and should be interpreted as decision support, not definitive business advice.
* AI-generated outputs depend on the KPI context provided to the model and may require independent verification.
* The project is a portfolio demonstration and is not intended for production financial reporting or automated business decisions.

## Author

**Mahek Radadiya**

GitHub: [Ma-hek01](https://github.com/Ma-hek01)

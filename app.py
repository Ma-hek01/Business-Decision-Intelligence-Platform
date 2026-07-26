import streamlit as st
from src.report_generator import generate_report
from src.llm import ask_llm
import pandas as pd
from src.analytics import executive_summary
from src.analytics import profit_by_region

from src.database import load_data
from src.analytics import (
    calculate_kpis,
    revenue_by_region,
    revenue_by_category,
    monthly_sales,
    top_products
)

import plotly.express as px

st.set_page_config(
    page_title="Business Decision Intelligence Platform",
    layout="wide"
)

st.title("📊 Business Decision Intelligence Platform")

st.caption(
    "AI-powered executive dashboard for business performance monitoring, KPI analytics and decision support."
)
# -----------------------------
# Load Data
# -----------------------------
df = load_data()

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

# -----------------------------
# Sidebar Filters
# -----------------------------
st.sidebar.header("Dashboard Filters")

selected_region = st.sidebar.multiselect(
    "Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

selected_category = st.sidebar.multiselect(
    "Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

selected_segment = st.sidebar.multiselect(
    "Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

selected_year = st.sidebar.multiselect(
    "Year",
    options=sorted(df["Order_Date"].dt.year.unique()),
    default=sorted(df["Order_Date"].dt.year.unique())
)

# -----------------------------
# Apply Filters
# -----------------------------
filtered_df = df[
    (df["Region"].isin(selected_region))
    &
    (df["Category"].isin(selected_category))
    &
    (df["Segment"].isin(selected_segment))
    &
    (df["Order_Date"].dt.year.isin(selected_year))
]

kpis = calculate_kpis(filtered_df)

# -----------------------------
# KPI Cards
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

col1.metric("Revenue", f"${kpis['Revenue']:,.0f}")
col2.metric("Profit", f"${kpis['Profit']:,.0f}")
col3.metric("Orders", kpis["Orders"])
col4.metric("Margin", f"{kpis['Profit Margin']}%")

col5, col6, col7, col8 = st.columns(4)

col5.metric("Customers", kpis["Customers"])
col6.metric("Avg Order", f"${kpis['Average Order Value']:,.0f}")
col7.metric("Best Region", kpis["Best Region"])
col8.metric("Best Category", kpis["Best Category"])
st.divider()

summary = executive_summary(filtered_df)

st.subheader("📌 Executive Decision Panel")

col1, col2 = st.columns(2)

with col1:
    st.metric("Business Health", summary["Health"])
    st.metric("Best Region", summary["Best Region"])
    st.metric("Best Category", summary["Best Category"])

with col2:
    st.metric("Top Product", summary["Top Product"])

    st.info(summary["Recommendation"])

# -----------------------------
# Revenue Trend
# -----------------------------
st.subheader("Monthly Revenue Trend")

monthly = monthly_sales(filtered_df)

fig = px.line(
    monthly,
    x="Month",
    y="Sales",
    markers=True
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Region + Category
# -----------------------------
left, right = st.columns(2)

with left:

    region = revenue_by_region(filtered_df)

    fig = px.bar(
        region,
        x="Region",
        y="Sales",
        title="Revenue by Region"
    )

    st.plotly_chart(fig, use_container_width=True)

with right:

    category = revenue_by_category(filtered_df)

    fig = px.pie(
        category,
        names="Category",
        values="Sales",
        title="Revenue by Category"
    )

    st.plotly_chart(fig, use_container_width=True)

st.subheader("Profit by Region")

profit = profit_by_region(filtered_df)

fig = px.bar(
    profit,
    x="Region",
    y="Profit",
    color="Profit",
    title="Profit by Region"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Top Products
# -----------------------------
st.subheader("Top 10 Products")

products = top_products(filtered_df)

fig = px.bar(
    products,
    x="Sales",
    y="Product_Name",
    orientation="h"
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

# st.header("Executive Business Summary")

region = revenue_by_region(filtered_df)
category = revenue_by_category(filtered_df)

report = generate_report(kpis, region, category)

st.subheader("📈 Executive Report")

summary, insight, recommendation = report.split("##")[1:]

col1, col2 = st.columns(2)

with col1:
    st.info("## Executive Summary\n" + summary)

with col2:
    st.warning("## Business Insight\n" + insight)

st.success("## Recommendation\n" + recommendation)

st.divider()

st.header("AI Business Assistant")

# -----------------------------
# Quick AI Prompts
# -----------------------------
col1, col2, col3 = st.columns(3)

if col1.button("📈 Summarize"):
    st.session_state["question"] = "Summarize business performance"

if col2.button("⚠️ Risks"):
    st.session_state["question"] = "Identify the biggest business risks"

if col3.button("💡 Recommendations"):
    st.session_state["question"] = "Recommend actions to improve business performance"

default_question = st.session_state.get("question", "")

# -----------------------------
# Text Input
# -----------------------------
question = st.text_input(
    "Ask a business question",
    value=default_question,
    placeholder="Example: Which region should receive more investment?"
)

if st.button("Ask AI"):

    if question.strip() == "":
        st.warning("Please enter a question.")
    else:

        with st.spinner("Analyzing business data..."):

            try:
                answer = ask_llm(
                    question,
                    kpis,
                    region,
                    category
                )

                st.markdown("## 🤖 AI Executive Analysis")
                st.info(answer)

            except Exception as e:
                st.error(e)
        
st.divider()

st.caption(
    "Business Decision Intelligence Platform | Python • SQLite • Plotly • Streamlit • Ollama"
)
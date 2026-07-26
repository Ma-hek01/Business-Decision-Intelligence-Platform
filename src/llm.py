import requests

OLLAMA_URL = "http://localhost:11434/api/generate"


def ask_llm(question, kpis, region_df, category_df):

    top_region = (
        region_df.iloc[0]["Region"]
        if not region_df.empty else "N/A"
    )

    top_category = (
        category_df.iloc[0]["Category"]
        if not category_df.empty else "N/A"
    )

    prompt = f"""
You are a Senior Business Intelligence Consultant.

The dashboard is filtered.

Business KPIs:

Revenue: ${kpis['Revenue']:,.2f}
Profit: ${kpis['Profit']:,.2f}
Profit Margin: {kpis['Profit Margin']}%
Orders: {kpis['Orders']}
Customers: {kpis['Customers']}
Average Order Value: ${kpis['Average Order Value']:,.2f}

Best Region: {top_region}
Best Category: {top_category}

User Question:
{question}

Provide:

1. Executive Summary
2. Business Insight
3. Recommendation

Keep the response under 150 words.
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3.2:3b",
            "prompt": prompt,
            "stream": False
        },
        timeout=120
    )

    response.raise_for_status()

    return response.json()["response"]
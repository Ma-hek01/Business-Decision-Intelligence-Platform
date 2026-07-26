import pandas as pd


def calculate_kpis(df):
    total_revenue = df["Sales"].sum()
    total_profit = df["Profit"].sum()
    total_orders = df["Order_ID"].nunique()
    total_customers = df["Customer_ID"].nunique()

    profit_margin = (
        (total_profit / total_revenue) * 100
        if total_revenue > 0 else 0
    )

    avg_order_value = (
        total_revenue / total_orders
        if total_orders > 0 else 0
    )

    # Handle empty filtered data
    if df.empty:
        best_region = "-"
        best_category = "-"
    else:
        best_region = (
            df.groupby("Region")["Sales"]
            .sum()
            .idxmax()
        )

        best_category = (
            df.groupby("Category")["Sales"]
            .sum()
            .idxmax()
        )

    return {
        "Revenue": round(total_revenue, 2),
        "Profit": round(total_profit, 2),
        "Orders": total_orders,
        "Customers": total_customers,
        "Profit Margin": round(profit_margin, 2),
        "Average Order Value": round(avg_order_value, 2),
        "Best Region": best_region,
        "Best Category": best_category
    }

    return {
        "Revenue": round(total_revenue, 2),
        "Profit": round(total_profit, 2),
        "Orders": total_orders,
        "Customers": total_customers,
        "Profit Margin": round(profit_margin, 2),
        "Average Order Value": round(avg_order_value, 2),
        "Best Region": best_region,
        "Best Category": best_category,
    }


def revenue_by_region(df):
    return (
        df.groupby("Region")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )


def revenue_by_category(df):
    return (
        df.groupby("Category")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
    )


def monthly_sales(df):

    df = df.copy()

    df["Order_Date"] = pd.to_datetime(df["Order_Date"])

    df["Month"] = df["Order_Date"].dt.to_period("M").astype(str)

    return (
        df.groupby("Month")["Sales"]
        .sum()
        .reset_index()
    )


def top_products(df):

    return (
        df.groupby("Product_Name")["Sales"]
        .sum()
        .reset_index()
        .sort_values("Sales", ascending=False)
        .head(10)
    )

def executive_summary(df):

    revenue_region = (
        df.groupby("Region")["Sales"]
        .sum()
        .idxmax()
    )

    profit_category = (
        df.groupby("Category")["Profit"]
        .sum()
        .idxmax()
    )

    top_product = (
        df.groupby("Product_Name")["Profit"]
        .sum()
        .idxmax()
    )

    margin = (
        df["Profit"].sum() /
        df["Sales"].sum()
    ) * 100

    if margin > 15:
        health = "🟢 Healthy"
    elif margin > 10:
        health = "🟡 Moderate"
    else:
        health = "🔴 Needs Attention"

    recommendation = (
        f"Increase investment in {revenue_region} "
        f"and focus on expanding {profit_category}."
    )

    return {
        "Health": health,
        "Best Region": revenue_region,
        "Best Category": profit_category,
        "Top Product": top_product,
        "Recommendation": recommendation
    }
    
def profit_by_region(df):

    return (
        df.groupby("Region")["Profit"]
        .sum()
        .reset_index()
        .sort_values("Profit", ascending=False)
    )
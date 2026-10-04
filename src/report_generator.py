def generate_report(kpis, region_df, category_df):
    top_region = (
        region_df.iloc[0]["Region"]
        if not region_df.empty else "N/A"
    )

    top_category = (
        category_df.iloc[0]["Category"]
        if not category_df.empty else "N/A"
    )

    report = f"""
# Executive Business Report

## Overall Performance

- Total Revenue: ${kpis['Revenue']:,.2f}
- Total Profit: ${kpis['Profit']:,.2f}
- Profit Margin: {kpis['Profit Margin']}%
- Orders Processed: {kpis['Orders']}
- Customers Served: {kpis['Customers']}

## Key Insights

- Best Performing Region: {top_region}
- Best Performing Category: {top_category}

## Recommendations

- Evaluate performance in {top_region}.
- Review profitability and growth opportunities in {top_category}.
- Review pricing and discount strategies for lower-performing areas.
- Continue monitoring monthly sales trends.
"""
    return report
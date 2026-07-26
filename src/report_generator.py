def generate_report(kpis, region_df, category_df):
    top_region = region_df.iloc[0]["Region"]
    top_category = category_df.iloc[0]["Category"]

    report = f"""
# Executive Business Report

## Overall Performance

• Total Revenue: ${kpis['Revenue']:,.2f}

• Total Profit: ${kpis['Profit']:,.2f}

• Profit Margin: {kpis['Profit Margin']}%

• Orders Processed: {kpis['Orders']}

• Customers Served: {kpis['Customers']}

## Key Insights

• Best Performing Region: {top_region}

• Best Performing Category: {top_category}

## Recommendations

• Increase investment in {top_region}.

• Expand the {top_category} product portfolio.

• Review pricing and discount strategy for lower-performing regions.

• Continue monitoring monthly sales trends.

"""
    return report
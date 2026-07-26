from src.database import load_data
from src.analytics import *

df = load_data()

print(calculate_kpis(df))

print("\n")

print(revenue_by_region(df))

print("\n")

print(revenue_by_category(df))

print("\n")

print(monthly_sales(df).head())

print("\n")

print(top_products(df))
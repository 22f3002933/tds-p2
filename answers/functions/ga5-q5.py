import pandas as pd
import json
from fuzzywuzzy import process
from collections import defaultdict

with open("sales_data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

# Convert JSON to DataFrame
df = pd.DataFrame(data)

# Step 1: Filter for "Shirt" and sales ≥ 194
df_filtered = df[(df['product'] == 'Shirt') & (df['sales'] >= 194)]

# Step 2: Normalize city names using fuzzy matching
unique_cities = df_filtered['city'].unique()
city_map = {}  # Dictionary to map incorrect city names to correct ones

# Set a reference city name list (could be based on most common names in dataset)
reference_cities = set(unique_cities)

# Apply fuzzy matching to cluster similar city names
for city in unique_cities:
    best_match, score = process.extractOne(city, reference_cities)
    if score > 85:  # Adjust threshold as needed
        city_map[city] = best_match
    else:
        city_map[city] = city  # Keep original if no good match

print(city_map)

# Step 3: Replace city names with standardized names
df_filtered['normalized_city'] = df_filtered['city'].map(city_map)

# Step 4: Aggregate sales by normalized city
sales_by_city = df_filtered.groupby('normalized_city')['sales'].sum()

# Step 5: Get sales for "Cairo"
cairo_sales = sales_by_city.get("Cairo", 0)
print(f"Total Shirt sales in Cairo (≥ 194 units per transaction): {cairo_sales}")

import pandas as pd
import datetime

def calculate_margin(excel_file, target_country, target_product, target_date):
    """
    Calculate margin for specific product/country up to a date.
    
    Args:
        excel_file: Path to the Excel file
        target_country: Country to filter for
        target_product: Product to filter for
        target_date: Date to filter up to (datetime object)
    """
    
    # Read the Excel file
    df = pd.read_excel(excel_file)
    
    # Clean up the data
    df = df.apply(lambda x: x.str.strip() if isinstance(x, pd.Series) and x.dtype == 'object' else x)
    
    # Clean up dates - handle both formats
    def parse_date(date_str):
        try:
            # Try MM-DD-YYYY format
            return pd.to_datetime(date_str, format='%m-%d-%Y')
        except:
            try:
                # Try YYYY/MM/DD format
                return pd.to_datetime(date_str, format='%Y/%m/%d')
            except:
                return None

    df['Date'] = df['Date'].apply(parse_date)
    
    # Clean up Sales and Cost columns
    df['Sales'] = df['Sales'].str.replace(' USD', '').str.strip().astype(float)
    df['Cost'] = df['Cost'].fillna(df['Sales'] * 0.5)  # Handle missing costs (50% of sales)
    df['Cost'] = df['Cost'].str.replace(' USD', '').str.strip().astype(float)
    
    # Clean up Product column (remove code after slash)
    df['Product'] = df['Product/Code'].str.split('/').str[0]
    
    # Create mapping for country variations
    country_mappings = {
        'US': ['USA', 'U.S.A', 'United States'],
        'AE': ['UAE', 'U.A.E', 'United Arab Emirates'],
        'UK': ['U.K', 'United Kingdom'],
        'IN': ['Ind', 'IND', 'India'],
        'BR': ['BRA', 'Bra', 'Brazil'],
        'FR': ['Fra', 'FRA', 'France']
    }
    
    # Standardize country names
    for standard, variants in country_mappings.items():
        df.loc[df['Country'].isin(variants), 'Country'] = standard
    
    # Filter the data
    filtered_df = df[
        (df['Country'] == target_country) &
        (df['Product'] == target_product) &
        (df['Date'] <= target_date)
    ]
    
    # Calculate total sales and costs
    total_sales = filtered_df['Sales'].sum()
    total_cost = filtered_df['Cost'].sum()
    
    # Calculate margin
    margin = (total_sales - total_cost) / total_sales if total_sales > 0 else 0
    
    return margin

# Example usage:
excel_file = "./q-clean-up-excel-sales-data.xlsx"  # Your downloaded Excel file
country = "FR"  # The value of v from your question
product = "Zeta"  # The value of w from your question
date = datetime.datetime.strptime("2022-05-20", "%Y-%m-%d")  # The value of S from your question

margin = calculate_margin(excel_file, country, product, date)
print(f"Margin: {margin:.4f}")  # or {margin*100:.2f}% as percentage
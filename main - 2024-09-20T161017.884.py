import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the real estate data from CSV
def load_data(file_path):
    """
    Loads real estate data from a CSV file.
    """
    data = pd.read_csv(file_path)
    return data

# Data cleaning
def clean_data(df):
    """
    Cleans and preprocesses the real estate data.
    """
    df = df.dropna()  # Drop rows with missing data
    df['Price'] = df['Price'].replace('[\$,]', '', regex=True).astype(float)  # Convert price to numeric
    df['Date Listed'] = pd.to_datetime(df['Date Listed'])  # Convert 'Date Listed' to datetime
    return df

# Analyze average listing price by neighborhood
def price_trends(df):
    """
    Shows average listing prices per neighborhood.
    """
    avg_price_neighborhood = df.groupby('Neighborhood')['Price'].mean().sort_values(ascending=False)
    return avg_price_neighborhood

# Analyze listing volume by neighborhood
def volume_trends(df):
    """
    Shows the number of listings per neighborhood.
    """
    listing_volume = df['Neighborhood'].value_counts()
    return listing_volume

# Visualize price trends in a bar chart
def plot_price_trends(avg_price_neighborhood):
    """
    Visualizes average listing price by neighborhood using a bar plot.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_price_neighborhood.index, y=avg_price_neighborhood.values)
    plt.xticks(rotation=90)
    plt.title('Average Listing Price by Neighborhood')
    plt.ylabel('Price ($)')
    plt.xlabel('Neighborhood')
    plt.tight_layout()
    plt.show()

# Visualize listing volume
def plot_listing_volume(volume):
    """
    Visualizes the listing volume per neighborhood.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=volume.index, y=volume.values, palette='coolwarm')
    plt.xticks(rotation=90)
    plt.title('Number of Listings by Neighborhood')
    plt.ylabel('Number of Listings')
    plt.xlabel('Neighborhood')
    plt.tight_layout()
    plt.show()

# Days on market analysis
def days_on_market_analysis(df):
    """
    Shows the median days on market by neighborhood.
    """
    median_days_on_market = df.groupby('Neighborhood')['Days on Market'].median().sort_values()
    return median_days_on_market

# Visualize days on market trends
def plot_days_on_market(median_days):
    """
    Plots the median days on market by neighborhood.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=median_days.index, y=median_days.values, palette='magma')
    plt.xticks(rotation=90)
    plt.title('Median Days on Market by Neighborhood')
    plt.ylabel('Days on Market')
    plt.xlabel('Neighborhood')
    plt.tight_layout()
    plt.show()

# Main function to execute analysis
def main():
    # Load and clean the data
    file_path = 'real_estate_data.csv'  # Example file path
    df = load_data(file_path)
    df = clean_data(df)
    
    # Price trends analysis
    avg_price_neighborhood = price_trends(df)
    print("Average Price by Neighborhood:\n", avg_price_neighborhood)
    plot_price_trends(avg_price_neighborhood)
    
    # Volume trends analysis
    volume = volume_trends(df)
    print("Listing Volume by Neighborhood:\n", volume)
    plot_listing_volume(volume)
    
    # Days on market analysis
    median_days = days_on_market_analysis(df)
    print("Median Days on Market by Neighborhood:\n", median_days)
    plot_days_on_market(median_days)

if __name__ == "__main__":
    main()

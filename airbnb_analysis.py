# 📦 Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# 🗂️ Load Excel File
file_path = "/Users/devlodhia/Desktop/1730285881-Airbnb_Open_Data.xlsx"
df = pd.read_excel(file_path)

# 🧹 Data Cleaning
df.dropna(subset=['name', 'host_name', 'neighbourhood_group', 'neighbourhood', 'room_type', 'price'], inplace=True)
df = df[df['price'] > 0]

# 🎯 Q1: Different Property Types
print("Room Types:", df['room_type'].unique())
sns.countplot(data=df, x='room_type', palette='Set2')
plt.title('Room Type Distribution')
plt.show()

# 🎯 Q2: Neighborhood Group with Most Listings
group_counts = df['neighbourhood_group'].value_counts()
print("Listings by Neighborhood Group:\n", group_counts)
group_counts.plot(kind='bar', color='skyblue')
plt.title('Listings by Neighborhood Group')
plt.show()

# 🎯 Q3: Highest Average Prices by Neighborhood Group
avg_price = df.groupby('neighbourhood_group')['price'].mean().sort_values(ascending=False)
print("Average Price by Neighborhood Group:\n", avg_price)
avg_price.plot(kind='bar', color='orange')
plt.title('Average Price by Neighborhood Group')
plt.show()

# 🎯 Q4: Construction Year vs Price (if column exists)
if 'year' in df.columns:
    sns.scatterplot(data=df, x='year', y='price')
    plt.title('Construction Year vs Price')
    plt.show()

# 🎯 Q5: Top 10 Hosts by Listing Count
top_hosts = df.groupby('host_name')['calculated_host_listings_count'].sum().sort_values(ascending=False).head(10)
print("Top 10 Hosts:\n", top_hosts)
top_hosts.plot(kind='bar', color='green')
plt.title('Top 10 Hosts by Listing Count')
plt.xticks(rotation=45)
plt.show()

# 🎯 Q6: Verified Identity vs Positive Reviews
if 'host_identity_verified' in df.columns and 'review_scores_rating' in df.columns:
    verified = df[df['host_identity_verified'] == 't']
    non_verified = df[df['host_identity_verified'] == 'f']
    print("Avg Rating (Verified):", verified['review_scores_rating'].mean())
    print("Avg Rating (Non-Verified):", non_verified['review_scores_rating'].mean())

# 🎯 Q7: Price vs Service Fee Correlation
if 'service_fee' in df.columns:
    correlation = df[['price', 'service_fee']].corr()
    print("Correlation:\n", correlation)
    sns.scatterplot(data=df, x='price', y='service_fee')
    plt.title('Price vs Service Fee')
    plt.show()

# 🎯 Q8: Review Rating by Neighborhood Group & Room Type
if 'review_scores_rating' in df.columns:
    rating_summary = df.groupby(['neighbourhood_group', 'room_type'])['review_scores_rating'].mean().unstack()
    print("Review Rating Summary:\n", rating_summary)
    sns.heatmap(rating_summary, annot=True, cmap='coolwarm')
    plt.title('Review Rating by Neighborhood Group & Room Type')
    plt.show()

# 🎯 Q9: Host Listing Count vs Availability
sns.scatterplot(data=df, x='calculated_host_listings_count', y='availability_365')
plt.title('Host Listing Count vs Availability')
plt.show()

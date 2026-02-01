import pandas as pd
import json
import sqlite3

# Load datasets
orders = pd.read_csv("orders.csv")
users = pd.read_csv("users.csv")
restaurants = pd.read_csv("restaurants.csv")

# Merge orders with users (LEFT JOIN)
orders_users = pd.merge(
    orders,
    users,
    on="user_id",
    how="left"
)

# Merge with restaurants (LEFT JOIN)
final_dataset = pd.merge(
    orders_users,
    restaurants,
    on="restaurant_id",
    how="left"
)

# Save final dataset
final_dataset.to_csv("final_food_delivery_dataset.csv", index=False)

print("Final dataset created successfully!")

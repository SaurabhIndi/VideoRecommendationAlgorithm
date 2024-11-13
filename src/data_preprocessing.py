# src/data_preprocessing.py
import pandas as pd
from api_integration import get_all_viewed_posts, get_all_liked_posts, get_all_user_ratings, get_all_posts

def preprocess_data():
    # Fetch data from API
    viewed_posts = get_all_viewed_posts()
    liked_posts = get_all_liked_posts()
    user_ratings = get_all_user_ratings()
    all_posts = get_all_posts()

    # Convert JSON data to DataFrames for easier processing
    viewed_df = pd.DataFrame(viewed_posts)
    liked_df = pd.DataFrame(liked_posts)
    ratings_df = pd.DataFrame(user_ratings)
    posts_df = pd.DataFrame(all_posts)

    # Handling missing data (simple example)
    posts_df.fillna({'rating': posts_df['rating'].mean()}, inplace=True)
    
    # Normalize ratings between 0 and 1 if needed
    if 'rating' in ratings_df.columns:
        ratings_df['normalized_rating'] = ratings_df['rating'] / ratings_df['rating'].max()

    # Save preprocessed data
    posts_df.to_csv("data/posts_preprocessed.csv", index=False)
    print("Data preprocessed and saved.")

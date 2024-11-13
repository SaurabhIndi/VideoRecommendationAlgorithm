# src/recommendation.py
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load preprocessed data
posts_df = pd.read_csv("data/posts_preprocessed.csv")

# Content-Based Filtering
def content_based_recommend(user_history, top_n=5):
    # Simple content-based recommendation using tags or metadata
    video_features = posts_df[['tag1', 'tag2']]  # Replace with actual metadata fields
    user_profile = user_history[['tag1', 'tag2']]  # Features of videos user interacted with

    similarity_matrix = cosine_similarity(user_profile, video_features)
    similarity_scores = similarity_matrix.mean(axis=0)

    # Get top N recommendations
    top_indices = similarity_scores.argsort()[-top_n:][::-1]
    recommended_videos = posts_df.iloc[top_indices]
    return recommended_videos

# Collaborative Filtering (Placeholder)
def collaborative_recommend(user_id, top_n=5):
    # Use collaborative filtering techniques here, like matrix factorization or SVD.
    # Placeholder implementation
    print(f"Collaborative recommendations for user {user_id} are being generated.")
    return []

# Hybrid Model
def hybrid_recommend(user_history, user_id, top_n=5):
    content_recs = content_based_recommend(user_history, top_n)
    collaborative_recs = collaborative_recommend(user_id, top_n)

    # Combine recommendations, here we assume content-based is more significant
    hybrid_recs = pd.concat([content_recs, collaborative_recs]).drop_duplicates().head(top_n)
    return hybrid_recs

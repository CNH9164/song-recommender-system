Song Recommender System

A content-based song recommender built on the Spotify Tracks dataset (114k songs). Pick a song, get 5 similar ones.
How it works
Each song gets a tag combining its artist name and genre. Those tags get vectorized using CountVectorizer (5000 features) and cosine similarity scores tell us how close any two songs are.
Tech Stack
Python, Pandas, Scikit-learn, Streamlit, Cosine Similarity
Dataset
Spotify Tracks Dataset — 114k tracks with metadata on artists, albums, and genres.


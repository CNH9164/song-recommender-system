import streamlit as st
import pickle
import pandas as pd

df = pd.DataFrame(pickle.load(open('song_dict.pkl', 'rb')))
similarity = pickle.load(open('song_similarity.pkl', 'rb'))

def recommend(song):
    idx = df[df['track_name'] == song].index[0]
    distances = similarity[idx]
    songs_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    return [df.iloc[i[0]].track_name for i in songs_list]

st.title('Song Recommender')

selected_song = st.selectbox('Pick a song', df['track_name'].values)

if st.button('Recommend'):
    for song in recommend(selected_song):
        st.write(song)

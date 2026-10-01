import streamlit as st

from similar_songs_demo import recommend_songs, songs


artists = sorted(songs["Artist"].drop_duplicates())
artist_name = st.selectbox("Artist", artists, index=None, placeholder="select an artist")

if artist_name:
    artist_songs = songs[songs["Artist"] == artist_name]
    tracks = sorted(artist_songs["Track"].drop_duplicates())
    track_name = st.selectbox("Song", tracks, index=None, placeholder="select a song")

    if track_name:
        st.write("Recommendations")
        recommendations = recommend_songs(artist_name, track_name, 5)
        st.dataframe(recommendations[["Artist", "Track"]], hide_index=True)

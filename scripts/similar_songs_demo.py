import pandas as pd


# these are the sound details we'll compare
features = [
    "Danceability",
    "Energy",
    "Acousticness",
    "Valence",
    "Tempo",
    "Loudness",
]

df = pd.read_csv("cleaned_dataset.csv")

# skip tracks missing one of these values
songs = df.dropna(subset=features + ["Artist", "Track"]).reset_index(drop=True)

# put each sound detail on the same scale so tempo doesn't overpower the others
scaled_features = (songs[features] - songs[features].min()) / (
    songs[features].max() - songs[features].min()
)


def recommend_songs(artist_name, track_name, number=5):
    matches = songs[
        (songs["Artist"].str.lower() == artist_name.lower())
        & (songs["Track"].str.lower() == track_name.lower())
    ]

    if matches.empty:
        print("couldn't find that song. check the artist and track name.")
        return

    # compare every track with the song we picked; a smaller distance means a closer match
    song_number = matches.index[0]
    distances = ((scaled_features - scaled_features.iloc[song_number]) ** 2).sum(axis=1) ** 0.5

    recommendations = songs[["Artist", "Track"]].copy()
    recommendations["distance"] = distances
    recommendations = recommendations.drop_duplicates(subset=["Artist", "Track"])
    recommendations = recommendations.drop(song_number)

    return recommendations.sort_values("distance").head(number)


# try a song from the dataset
recommendations = recommend_songs("Gorillaz", "Feel Good Inc.")
print(recommendations[["Artist", "Track"]].to_string(index=False))

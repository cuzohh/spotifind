# similar songs app

the app is a small way to try the recommender without typing song names by hand.

## open the app

open a terminal in the project folder and run:

```sh
python -m pip install pandas streamlit
streamlit run scripts/similar_songs_app.py
```

## pick a song

type in the artist box to search the artists in `cleaned_dataset.csv`, then choose one from the list. the song box will show songs by that artist. type there to search, then choose a song from the list.

these are searchable dropdowns, so you can only select an artist and song that are in the dataset. after you pick a song, the app shows five similar songs underneath.

some songs have a separate row for each artist in the csv. the recommendation list puts those rows together, so the same track only shows once with its artists listed together.

the app compares danceability, energy, acousticness, valence, tempo, and loudness. it scales these details so each one has a similar effect, then finds songs with the closest values. this means similar by those details in the dataset, not necessarily songs everyone will like.

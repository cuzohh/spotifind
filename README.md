# spotifind

project about music recommendations. it has a group notebook, a quick data check, and a simple demo that finds songs with similar sound details.

## files and folders

- `cleaned_dataset.csv` has song details, sound features, Spotify streams, and YouTube views and likes.
- `Spotifind.ipynb` is the main project notebook for the group. it stays in the project folder.
- `docs/possible project questions.md` has ideas for the project question.
- `docs/similar songs app.md` explains how the simple app works.
- `notebooks/data_audit.ipynb` checks for missing values and repeated tracks, then makes a few charts.
- `scripts/similar_songs_demo.py` finds tracks that sound similar to a song you choose.
- `scripts/similar_songs_app.py` is a small app for picking a song and seeing recommendations.
- `LICENSE` has the license information for this project.

## try the simple app

you need python, pandas, and streamlit. open a terminal in the project folder and run:

```sh
python -m pip install pandas streamlit
streamlit run scripts/similar_songs_app.py
```

the artist and song boxes let you search through choices from the csv as you type. pick an artist first, then pick one of that artist's songs. the recommendations show up after you pick a song. you can only choose artists and songs that are in the dataset. see [the app guide](docs/similar%20songs%20app.md) for more detail.

## try the similar songs demo

you need python and pandas. open a terminal in the project folder and run:

```sh
python -m pip install pandas
python scripts/similar_songs_demo.py
```

the demo asks for an artist name and song name. enter them as they appear in the csv and it will show five similar tracks. to get three instead, add `3` as the third value in the call near the bottom of `scripts/similar_songs_demo.py`:

```python
recommendations = recommend_songs(artist_name, track_name, 3)
```

the demo compares danceability, energy, acousticness, valence, tempo, and loudness. it puts them on the same scale, then finds tracks with the closest values. this finds songs that are similar in the data. it can't tell us if someone will actually like them.

## open the data check

open `notebooks/data_audit.ipynb` in jupyter or your notebook editor. keep the project folder as the working folder so the notebook can find the csv. it uses pandas and matplotlib:

```sh
python -m pip install pandas matplotlib
```

## about the data

the csv appears to be based on the [spotify and youtube dataset on kaggle](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube). check the dataset notes for the original data sources and cite them in the final project. the rows in this file are only the songs included in the dataset, so conclusions may not apply to all music.

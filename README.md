# spotifind

this is a small class project about music recommendations. it has a group notebook, a quick data check, and a simple demo that finds songs with similar sound details.

## what's in here

- `cleaned_dataset.csv` has song details, sound features, Spotify streams, and YouTube views and likes.
- `Spotifind.ipynb` is the main project notebook for the group.
- `data_audit.ipynb` takes a quick look at missing values, repeated tracks, and a few charts.
- `similar_songs_demo.py` finds a few tracks that sound similar to a song you choose.
- `possible project questions.md` has some ideas for the project question.
- `LICENSE` has the license information for this project.

## try the similar songs demo

you need python and pandas. from the project folder, run:

```sh
python -m pip install pandas
python similar_songs_demo.py
```

the demo starts with "feel good inc." by gorillaz. to try another song, change the artist and track name near the bottom of `similar_songs_demo.py`:

```python
recommendations = recommend_songs("Gorillaz", "Feel Good Inc.")
```

you can also change the number of suggestions. for example, `recommend_songs("Artist", "Song", 3)` asks for three.

the demo compares danceability, energy, acousticness, valence, tempo, and loudness. it puts them on the same scale, then finds tracks with the closest values. this finds songs that are similar in the data. it can't tell us if someone will actually like them.

## open the data check

open `data_audit.ipynb` in jupyter or your notebook editor and run the cells from the project folder. it uses pandas and matplotlib:

```sh
python -m pip install pandas matplotlib
```

## about the data

the csv appears to be based on the [spotify and youtube dataset on kaggle](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube). check the dataset notes for the original data sources and cite them in the final project. the rows in this file are only the songs included in the dataset, so conclusions may not apply to all music.

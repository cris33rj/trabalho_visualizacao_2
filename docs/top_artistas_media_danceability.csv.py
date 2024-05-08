# %%
import numpy as np 
import pandas as pd 
import sys

# %%
spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')


# %%
caracteristicas = ['danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'liveness_%', 'speechiness_%','valence_%']


# %%
top_artistas = spotify_data['artist(s)_name'].value_counts().head(10).index

top_artistas_data = spotify_data[spotify_data['artist(s)_name'].isin(top_artistas)]

# %%
artista_caracteristica_media = top_artistas_data.groupby('artist(s)_name')['danceability_%'].mean().sort_values(ascending=False)


# %%
columns = ['artista', 'media']

df_artista_caracteristica_media = pd.DataFrame(list(artista_caracteristica_media.items()), columns=columns)


df_artista_caracteristica_media.to_csv(sys.stdout,header=True,index=False)

# %%




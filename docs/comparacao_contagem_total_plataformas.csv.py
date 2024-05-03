# %%
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import sys

# %%
# Attempting to load the dataset using 'ISO-8859-1' encoding
spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

# Displaying the first few rows of the dataset
#spotify_data.head()


# %%
def remover_virgula(string):
    if isinstance(string, str):
        string = float(string.replace(",", ""))        
    return string 

# %%
spotify_data['in_deezer_playlists'] = spotify_data['in_deezer_playlists'].apply(remover_virgula)
teste = spotify_data['in_deezer_playlists'].sum()
#print(teste)

# %%
#spotify_data['in_deezer_charts'] = spotify_data['in_deezer_charts'].apply(remover_virgula)
#teste = spotify_data['in_deezer_charts'].sum()
#print(teste)

# %%
spotify_data['in_shazam_charts'] = spotify_data['in_shazam_charts'].apply(remover_virgula)

#teste3 = spotify_data['in_shazam_charts'].sum()
#print(teste3)

# %%
# Calculating the total count of tracks present in playlists/charts for Spotify and Apple Music
total_counts = {
    'Spotify': spotify_data['in_spotify_playlists'].sum() + spotify_data['in_spotify_charts'].sum(),
    'Apple Music': spotify_data['in_apple_playlists'].sum() + spotify_data['in_apple_charts'].sum(),
    'Deezer Music': spotify_data['in_deezer_playlists'].sum() + spotify_data['in_deezer_charts'].sum(),
    'Shazam Music': spotify_data['in_shazam_charts'].sum()
}




# %%
#print(total_counts)

# %%
columns = ['plataforma', 'contagem']

# Create a DataFrame
#df_total_counts = pd.DataFrame(total_counts, index=total_counts.keys(), data=total_counts.values(), columns=columns)
df_total_counts  = pd.DataFrame(list(total_counts.items()), columns=['plataforma', 'contagem'])

# %%
df_total_counts.head()

# %%
#df_total_counts_spotify_apple_deezer_shazam.head()

# %%
df_total_counts.to_csv(sys.stdout,header=True,index=False)



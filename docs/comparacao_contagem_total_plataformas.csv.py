# %%
import numpy as np 
import pandas as pd 
import sys

# %%
# 
spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')



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


# %%
spotify_data['in_shazam_charts'] = spotify_data['in_shazam_charts'].apply(remover_virgula)


# %%
total_counts = {
    'Spotify': spotify_data['in_spotify_playlists'].sum() + spotify_data['in_spotify_charts'].sum(),
    'Apple Music': spotify_data['in_apple_playlists'].sum() + spotify_data['in_apple_charts'].sum(),
    'Deezer Music': spotify_data['in_deezer_playlists'].sum() + spotify_data['in_deezer_charts'].sum(),
    'Shazam Music': spotify_data['in_shazam_charts'].sum()
}




# %%


# %%
columns = ['plataforma', 'contagem']

df_total_counts  = pd.DataFrame(list(total_counts.items()), columns=['plataforma', 'contagem'])

# %%
df_total_counts.head()

# %%

# %%
df_total_counts.to_csv(sys.stdout,header=True,index=False)


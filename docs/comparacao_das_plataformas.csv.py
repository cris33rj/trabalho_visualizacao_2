# %%
import numpy as np 
import pandas as pd 
import sys

spotify_data = pd.read_csv('docs/data/spotify-2023.csv', encoding='ISO-8859-1')

def remover_virgula(string):
    if isinstance(string, str):
        string = float(string.replace(',', ''))        
    return string 

spotify_data['in_spotify_playlists'] = spotify_data['in_spotify_playlists'].apply(remover_virgula)

spotify_data['in_apple_playlists'] = spotify_data['in_apple_playlists'].apply(remover_virgula)

spotify_data['in_deezer_playlists'] = spotify_data['in_deezer_playlists'].apply(remover_virgula)

spotify_data['in_spotify_charts'] = spotify_data['in_spotify_charts'].apply(remover_virgula)

spotify_data['in_apple_charts'] = spotify_data['in_apple_charts'].apply(remover_virgula)

spotify_data['in_deezer_charts'] = spotify_data['in_deezer_charts'].apply(remover_virgula)

spotify_data['in_shazam_charts'] = spotify_data['in_shazam_charts'].apply(remover_virgula)

total_counts = {
    'Plataforma': pd.Series(
                        [
                            'Spotify',
                            'Apple',
                            'Deezer',
                            'Shazam'
                        ], index=
                            [
                                'Spotify','Apple','Deezer','Shazam'
                            ]
                    ),
    'charts': pd.Series(
                        [
                            spotify_data['in_spotify_charts'].sum(), 
                            spotify_data['in_apple_charts'].sum(),
                            spotify_data['in_deezer_charts'].sum(),
                            spotify_data['in_shazam_charts'].sum()
                        ], index=
                            [
                                'Spotify','Apple','Deezer','Shazam'
                            ]
                    ),
    'playlist': pd.Series(
                        [
                            spotify_data['in_spotify_playlists'].sum(),
                            spotify_data['in_apple_playlists'].sum(),
                            spotify_data['in_deezer_playlists'].sum(),                            
                            0
                        ], index=
                            [
                                'Spotify','Apple','Deezer','Shazam'
                            ]
                        ),
   
}

df_total_counts  = pd.DataFrame(total_counts)

df_total_counts.head()

df_total_counts.to_csv(sys.stdout,header=True,index=True)


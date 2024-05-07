<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
    li,ul,ol
    {
        text-align: justify;
        max-width:none;
        text-wrap: pretty;
    }
</style>

# 1.1 - Apresentação

### O trabalho:

Este trabalho de pesquisa foi produzido no curso de Mestrado em Computação - PGC UFF, como atividade parcial para cumprimento da disciplina de VISUALISAÇÃO DE DADOS (SI & PGC - UFF), ministrado pelo Professor Marcos Lage.

### Os alunos:

<div class="grid grid-cols-1">    
<div class="card" >

| Edel Melo          | Cristiano Nascimento          |
| :----:             |    :----:           |
| Aluno de Mestrado <BR> Mat. M048.123.012  | Aluno de Mestrado <br> Mat. M048.123.010  |
| <address><a href="mailto:edelmelo@id.uff.br">edelmelo@id.uff.br</a></address> | <address><a href="mailto:cristiano_nascimento@id.uff.br">mailto:cristiano_nascimento@id.uff.br</a></address> |

</div>
</div>

### A tarefa:

A tarefa consistia em fazer análises sobre um conjunto de dados disponibilizado no **Site Kaggle**, com o objetivo de responder a três perguntas:

1. Existe alguma característica que faz uma música ter mais chance de se tornar popular?
2. O conjunto das top 10 músicas e dos top 10 artistas varia muito se considerarmos apenas musicas lançadas no mesmo ano?
3. Discuta as diferenças entre as plataformas: Spotify, Deezer, Apple Music e Shazam?

### A base de dados:

O conjunto de dados foi disponibilizado no endereço: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023, 
e continha uma lista abrangente das músicas mais famosas de 2023 listadas no Spotify. O conjunto de dados oferecia uma variedade de recursos além do que normalmente está disponível em conjuntos de dados semelhantes. Ele possuia 954 registros, incluindo o nome dos campos, e estava em formato CVS (texto com campos separados por vígulas).

Conforme o **Site kaggle**, o *DATASET* apresentava os seguintes campos:

- **track_name** : Nome da música;
- **artist(s)_name** : Nome do(s) artista(s) da música;
- **artist_count** : número de artistas que contribuíram para a música;
- **release_year** : Ano em que a música foi lançada;
- **release_month** : Mês em que a música foi lançada;
- **release_day** : Dia do mês em que a música foi lançada;
- **in_spotify_playlists** : Número de *playlists* do Spotify nas quais a música está incluída;
- **in_spotify_charts** : Presença e classificação da música nas paradas do Spotify;
- **streams** : número total de streams no Spotify;
- **in_apple_playlists** : número de *playlists* do Apple Music nas quais a música está incluída;
- **in_apple_charts** : Presença e classificação da música nas paradas musicais da Apple;
- **in_deezer_playlists** : Número de *playlists* do Deezer em que a música está incluída;
- **in_deezer_charts** : Presença e posição da música nas paradas da Deezer;
- **in_shazam_charts** : Presença e classificação da música nas paradas do Shazam;
- **bpm** : Batidas por minuto, uma medida do andamento da música;
- **key** : tom da música;
- **mode** : Modo da música (maior ou menor);
- **danceability_%** : Porcentagem que indica quão adequada a música é para dançar;
- **valence_%** : Positividade do conteúdo musical da música;
- **energy_%** : Nível de energia percebido da música;
- **acousticness_%** : quantidade de som acústico na música;
- **instrumentalness_%** : Quantidade de conteúdo instrumental na música;
- **liveness_%** : Presença de elementos de performance ao vivo; e
- **Speechiness_%** : Quantidade de palavras faladas na música.


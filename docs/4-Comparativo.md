<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>
# 2.3 - Comparativo
## Análise comparativa entre as plataformas: Spotify, Deezer, Apple Music e Shazam.

Esta análise visa responder a seguinte questão: O conjunto das top 10 músicas e dos top 10 artistas varia muito se considerarmos apenas musicas lançadas no mesmo ano?

Para respondê-la, desenvolvemos quatro histogramas e dividimo-los em dois grupos: os que analisam os cantores e os que analisam as músicas.

Para os que analisam os cantores, temos:
<center>
<div class="grid" style="width: 500px;text-align: center;">
    <div id="ex01" class="card">
        <h4>Comparação da contagem total de músicas presentes nas playlists e charts das plataformas. (A1)</h4>
   <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex01(divWidth)) }
        </div>
    </div>
</div>
</center>
<div class="grid grid-cols-2" style="text-align: center; ">
    <div id="ex02" class="card">
        <h4>Músicas top 10 do Spotify com base no total de músicas presentes em playlists e charts. (A2)</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex02(divWidth-205)) }
        </div>
    </div>
    <div id="ex03" class="card">
        <h4>Músicas top 10 da Apple com base no total de músicas presentes em playlists e charts. . B1</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex03(divWidth-160)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Músicas top 10 do Deezer com base no total de músicas presentes em playlists e charts. B2</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex04(divWidth-210)) }
        </div>
    </div>
    <div id="ex05" class="card">
        <h4>Músicas top 10 do Shazam com base no total de músicas presentes em playlists e charts. B2</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex05(divWidth-210)) }
        </div>
    </div>
</div>

Os histogramas acima denominados B1 e B2, representam, respectivamente, as 10 músicas mais ouvidas se considerado todo o período disponibilizado no banco de dados disponibilizado no endereço: https://www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023 e as 10 mais ouvidas se considerado apenas aquelas lançadas no ano de 2023, mesmo ano do banco de dados anteriormente mencionado.

#### Ao analisá-los, respondemos que SIM, houve 80% de variação da composição das 10 músicas mais ouvidos.

```js
const divWidth = Generators.width(document.querySelector("#ex02"));
const divheight = 300;

import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";
import { showCode } from './showCode.js'; 

const vl = vegaLiteApi.register(vega, vegaLite);

const spotify = await FileAttachment("./data/spotify-2023.json").json({typed: true});

showCode(FileAttachment("./comparacao_contagem_total_plataformas.csv.py"))
const comparacao_contagem_plataformas = await FileAttachment("./comparacao_contagem_total_plataformas.csv").csv({typed: true});

showCode(FileAttachment("./top_10_songs_spotify_playlists_charts.csv.py"))
const top_10_songs_spotify_playlists_charts = await FileAttachment("./top_10_songs_spotify_playlists_charts.csv").csv({typed: true});

showCode(FileAttachment("./top_10_songs_apple_playlists_charts.csv.py"))
const top_10_songs_apple_playlists_charts = await FileAttachment("./top_10_songs_apple_playlists_charts.csv").csv({typed: true});

showCode(FileAttachment("./top_10_songs_deezer_playlists_charts.csv.py"))
const top_10_songs_deezer_playlists_charts = await FileAttachment("./top_10_songs_deezer_playlists_charts.csv").csv({typed: true});

showCode(FileAttachment("./top_10_songs_shazam_playlists_charts.csv.py"))
const top_10_songs_shazam_playlists_charts = await FileAttachment("./top_10_songs_shazam_playlists_charts.csv").csv({typed: true});

function ex01(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: comparacao_contagem_plataformas 
            },
            title: "A1",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {
                    "field": "plataforma", 
                    "type": "nominal",
                    "axis": {
                        "labelAngle": 45  // Set the angle to 45 degrees
                    }
                },
                "y": {
                    "field": "contagem", 
                    "type": "quantitative",
                    "scale": {"domain": [0, 5500000]}
                }
            }            
        }
    }
}

function ex02(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_10_songs_spotify_playlists_charts 
            },
            title: "A2",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "spotify_total", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 45  // Set the angle to 45 degrees
                    }
                },
                "y": {
                    "field": "track_name", 
                    "type": "nominal"                    
                }
            }            
        }
    }
}

function ex03(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_10_songs_apple_playlists_charts 
            },
            title: "A3",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "apple_total", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 45  // Set the angle to 45 degrees
                    }
                },
                "y": {
                    "field": "track_name", 
                    "type": "nominal"                    
                }
            }            
        }
    }
}

function ex04(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_10_songs_deezer_playlists_charts 
            },
            title: "A4",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "deezer_total", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 45  // Set the angle to 45 degrees
                    }
                },
                "y": {
                    "field": "track_name", 
                    "type": "nominal"                    
                }
            }            
        }
    }
}

function ex05(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_10_songs_shazam_playlists_charts 
            },
            title: "A5",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "shazam_total", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    }
                },
                "y": {
                    "field": "track_name", 
                    "type": "nominal"                    
                }
            }            
        }
    }
}
```
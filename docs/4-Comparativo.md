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

Esta análise visa responder a seguinte questão: <b> Discuta as diferenças entre as plataformas (Spotify, Deezer, Apple Music e Shazam)?</b>

Para a discussão, desenvolvemos 4 conjuntos de visualizações diferentes: <b>1)</b> Visualização A1 comparando o total de "streams" das 4 plataformas de música; <b>2)</b> Visualizações A2 a A5 com as 10 músicas top em cada plataforma, com base na presença delas em playlistas e charts; <b>3)</b> Matrizes de "scatterplots" exibindo dispersões em pares entre as variáveis "streams","in_spotify_playlists", "in_apple_playlists" e "in_deezer_playlists". Observação: Não consta o campo de playlists para Shazam; <b>4)</b> Matrizes de "scatterplots" exibindo dispersões em pares  entre as variáveis "streams",  "in_spotify_charts", "in_apple_charts", "in_deezer_charts" e "in_shazam_charts".

A motivação do uso das visualizações, assim como suas análises, poderão ser vistas na parte superior de cada visualizaçao. 

<b>1)</b> Visualização A1 comparando o total de "streams" das 4 plataformas de música;
<br>
Para a comparação optou-se pelo gráfico de barras por sua capacidade de evidenciar diferenças entre grandezas quantitativas. Nesse sentido, percebe-se que o Spotify impressiona pela sua superioridade em "streams", em comparação com as outras plataformas. Enquanto o Deezer, Apple e Shazam- têm um total de no máximo 500 mil streams, o spotify totaliza praticamente 5 milhões de streams.  


<center>
<div class="grid" style="width: 500px;text-align: center;">
    <div id="ex01" class="card">
        <h4>Comparação do total de "streams" entre as quatro plataformas. (A1)</h4>
   <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex01(divWidth)) }
        </div>
    </div>
</div>
</center>
<br>
<br>
<b>2)</b> Visualizações A2 a A5 com as 10 músicas top em cada plataforma, com base na presença delas em playlistas e charts:
<br>
Para a comparação optou-se pelo gráfico de barras pelos mesmos motivos mencionados no gráfico anterior. Percebe-se nas visualizações que as listas das 10 músicas top das plataformas são notavelmente diferentes. <br><br>
Nesse sentido, podem ser encontradas músicas que figuram em no máximo em 2 playlists/charts, sendo o caso de : "Get Lucky - Radio Edit" (Spotify e Deezer), "Smell Like Teen Spirit" (Spotify e Deezer), "Blinding Lights (Spotify e Apple)", "Onde Dance" ( Spotify e Apple) e "Somebody That I Used to Know" (Spotify e Deezer). E, em todos esses casos, consta pela menos uma música do Spotify, evidenciando que essa plataforma espelha consideravelmente a tendência do público. 
Importante notar também que as 10 músicas top do Spotify exibem uma certa proximidade entre si, no que tange à quantidade de "streams" enquanto nas outras plataformas a distância no total de "streams" é bem maior, especialmente a partir da segunda música. 


<div class="grid grid-cols-2" style="text-align: center; ">
    <div id="ex02" class="card">
        <h4>Músicas top 10 do Spotify com base no total de músicas presentes em playlists e charts. (A2)</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex02(divWidth-205)) }
        </div>
    </div>
    <div id="ex03" class="card">
        <h4>Músicas top 10 da Apple com base no total de músicas presentes em playlists e charts. (A3)</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex03(divWidth-160)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Músicas top 10 do Deezer com base no total de músicas presentes em playlists e charts. (A4)</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex04(divWidth-210)) }
        </div>
    </div>
    <div id="ex05" class="card">
        <h4>Músicas top 10 do Shazam com base no total de músicas presentes em playlists e charts. (A5)</h4>
        <div style="width: 100%; margin-top: 15px;">
             ${ vl.render(ex05(divWidth-210)) }
        </div>
    </div>
    </div>

<b>3)</b> Matrizes de "scatterplots" exibindo dispersões em pares entre as variáveis "streams","in_spotify_playlists", "in_apple_playlists" e "in_deezer_playlists":
<br>
Essa visualização foi selecionada com o fim de identificar as correlações positivas, negativas ou inexistentes entre as 4 plataformas especificamente no que refere-se às quatro variáveis mencionadas. A partir desse trabalho algumas perguntas podem ser respondidas, por exemplo: "Quando a presença de uma música aumenta na playlist de uma determinada plataforma, a quantidade de "streams" dessa música aumenta também?" ou "Quando a presença de uma música aumenta em playlists da Apple, ela também aumenta em playlists do Spotify". 
<br><br>
A primeira conclusão é que em geral, quando aumenta a presença de uma música em playlists de uma plataforma, a quantidade de streams associado aumenta também. Percebe-se essa tendência de maneira mais forte no Apple e de uma forma mais fraca no Deezer, onde é possivel identificar uma quantidade significativa de músicas que, não obstante constarem em inúmeras playlists, não são muito tocadas.
<br><br>
Quanto às variáveis relativas às playlists, percebe-se, em geral, a tendência da presença de uma música aumentar nas playlists do Deezer e Apple, quando se verifica seu aumento no Spotify. Essa tendência é mais forte quando envolve Deezer e Spotify. O mesmo não pode ser considerado,necessariamente, quando se trata do gráfico relativo ao Deezer e à Apple. Nele é possível verificar que muitas músicas com alta presença em playlists do Deezer são pouco frequentes em playlists da Apple.  
    <div id="ex06" class="card" style="width: 110%;">
        <h4>Playlists e streams: Relações aos pares. B1</h4>
        <div style="width: 110%; margin-top: 15px;">
             ${ vl.render(ex06(divWidth)) }
        </div>
    </div>
    <div></div>
<b>4)</b> Matrizes de "scatterplots" exibindo dispersões em pares  entre as variáveis "streams",  "in_spotify_charts", "in_apple_charts", "in_deezer_charts" e "in_shazam_charts":
<br>
Essa visualização foi selecionada com o fim de identificar as correlações positivas, negativas ou inexistentes entre as 4 plataformas especificamente no que refere-se às cinco variáveis mencionadas. A partir desse trabalho algumas perguntas podem ser respondidas, por exemplo: "Quando a presença de uma música aumenta no chart de uma determinada plataforma, a quantidade de "streams" dessa música aumenta também?" ou "Quando a presença de uma música aumenta no chart do Deezer, ela também aumenta no chart do Shazam?". 
<br><br>
A primeira conclusão é que em geral não é possível encontrar uma correlação significativa entre presença em charts e total de streams quando se considera todas as plataformas. A Apple é a que consegue destacar um pouco melhor, porém com maior parte dos pontos comprimidos na area entre a parte inferior do eixo y e a parte esquerda do eixo x do gráfico. 
<br><br>
Quanto às variáveis relativas às charts em si, não se pode afirmar que há um correlação satistória entre as quatro plataformas. Apenas no caso de Deezer e Spotify que é possível encontrar uma dispersão um pouco melhor.      
    <div id="ex07" class="card" style="width: 110%;">
        <h4>Charts e streams: Relações aos pares. B1</h4>
        <div style="width: 110%; margin-top: 15px;">
             ${ vl.render(ex07(divWidth)) }
        </div>
    </div>

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

function ex01(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: comparacao_contagem_plataformas
            },
            "transform": [{"filter": "datum.contagem > 0 "}],
            title: "A1",
            "mark": 
            {
                "type": "bar",
                "size": 60,
            },                
            "encoding": 
            {
                "color": {"value": "gray"},
                "x": 
                {
                   "field": ["plataforma"],
                    "type": "nominal",                     
                    "title": "Nome da plataforma",
                    "sort": 
                    {
                        "field": "contagem",
                        "order": "descending"
                    },
                    "axis": {"labelAngle": 45}
                },
                "y": 
                {
                   "field": ["contagem"],
                    "aggregate": "sum",
                    "type": "quantitative",
                    "title": "Total de Streams",
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
            "transform": [{"filter": "datum.spotify_total > 0 "}],
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
                    "type": "nominal",
                    "sort": {
                        "field": "spotify_total",
                        "order": "descending"
                    },                    
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
            "transform": [{"filter": "datum.apple_total > 0 "}],
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
                    "type": "nominal",
                    "sort": {
                        "field": "apple_total",
                        "order": "descending"
                    },                   
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
            "transform": [{"filter": "datum.deezer_total > 0 "}],
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
                    "type": "nominal",
                    "sort": {
                        "field": "deezer_total",
                        "order": "descending"
                    },                    
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
            "transform": [{"filter": "datum.shazam_total > 0 "}],
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
                    "type": "nominal",
                    "sort": {
                        "field": "shazam_total",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex06(divWidth) {
    return {
        spec: {
            "repeat": {
            "row": ["streams","in_spotify_playlists","in_apple_playlists",  "in_deezer_playlists"],
            "column": ["streams","in_spotify_playlists", "in_apple_playlists",  "in_deezer_playlists"]
            },          
            data: {
                values: spotify 
            },            
            spec: {
            width: 120,
            height: 120,
            "mark": "point",            
            "encoding": {
                "x": {"field": {"repeat": "column"}, "type": "quantitative"},
                "y": {"field": {"repeat": "row"}, "type": "quantitative"}
            }                     
        }
        }
    }
}

function ex07(divWidth) {
    return {
        spec: {
            "repeat": {
            "row": ["streams","in_spotify_charts","in_apple_charts",  "in_deezer_charts"],
            "column": ["streams","in_spotify_charts", "in_apple_charts",  "in_deezer_charts","in_shazam_charts"]
            },          
            data: {
                values: spotify 
            },            
            spec: {
            width: 120,
            height: 120,
            "mark": "point",            
            "encoding": {
                "x": {"field": {"repeat": "column"}, "type": "quantitative"},
                "y": {"field": {"repeat": "row"}, "type": "quantitative"}
            }                     
        }
        }
    }
}


```
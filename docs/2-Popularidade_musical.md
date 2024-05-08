<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>
# 2.1 - Popularidade Musical

## Análise do que faz uma música ser popular.

Esta análise visa responder a seguinte questão: <b>Existe alguma característica que faz uma música ter mais chance de se tornar popular? </b>

Para respondê-la, geramos oito scatter plots que com o objetivo de observar a relação da variável "Streams" com "Danceability", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness" e "BPM", respectivamente. Os gráficos que apresentam uma tendência mais forte, indicando características presentes em músicas populares são: "Streams X Danceability" e "Streams X Energy". O gráfico "Streams X Speechiness" apresenta também uma tendência, mas de forma inversa. 

Nos dois primeiros gráficos apontados é possível perceber que "Streams" (em bilhões) mostra uma tendência de aumento à medida que "Danceability" e "Energy" crescem. Quanto ao gráfico "Streams X Speechiness", percebe-se no gráfico que a maior parte dos pontos se concentram na parte esquerda, evidenciando que músicas com baixa "speechiness" têm um grande número de streams sendo, portanto, mais populares. Por outro lado, à medida que “speechiness” aumenta, há menos pontos, sugerindo que músicas com alta “speechiness” geralmente não são tão populares.

<div class="grid grid-cols-2">
    <div id="ex01" class="card">
        <h4>Danceability X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex01(divWidth - 30)) }
        </div>
    </div>  
    <div id="ex02" class="card">
        <h4>Valence X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex02(divWidth - 30)) }
        </div>
    </div>
    <div id="ex03" class="card">
        <h4>Energy X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex03(divWidth - 30)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Acousticness X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex04(divWidth - 30)) }
        </div>
    </div>
     <div id="ex05" class="card">
        <h4>Instrumentalness X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex05(divWidth - 30)) }
        </div>
    </div>
    <div id="ex06" class="card">
        <h4>Liveness X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex06(divWidth - 30)) }
        </div>
    </div>
     <div id="ex07" class="card">
        <h4>Speechiness X Streams.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex07(divWidth - 30)) }
        </div>    
</div>

```js
const divWidth = Generators.width(document.querySelector("#ex01"));

import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";
import { showCode } from './showCode.js'; 

const vl = vegaLiteApi.register(vega, vegaLite);

const spotify = await FileAttachment("./data/spotify-2023.csv").csv({typed: true})

showCode(FileAttachment("./top_artistas_media_danceability.csv.py"))
const top_artistas_media_danceability = await FileAttachment("./top_artistas_media_danceability.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_energy.csv.py"))
const top_artistas_media_energy = await FileAttachment("./top_artistas_media_energy.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_speechiness.csv.py"))
const top_artistas_media_speechiness = await FileAttachment("./top_artistas_media_speechiness.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_valence.csv.py"))
const top_artistas_media_valence = await FileAttachment("./top_artistas_media_valence.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_liveness.csv.py"))
const top_artistas_media_liveness = await FileAttachment("./top_artistas_media_liveness.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_acousticness.csv.py"))
const top_artistas_media_acousticness = await FileAttachment("./top_artistas_media_acousticness.csv").csv({typed: true});

showCode(FileAttachment("./top_artistas_media_instrumentalness.csv.py"))
const top_artistas_media_instrumentalness = await FileAttachment("./top_artistas_media_instrumentalness.csv").csv({typed: true});


function ex01(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A1",
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "danceability_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}

function ex02(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A2",            
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "valence_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}

function ex03(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A3",        
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "energy_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}

function ex04(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A4",            
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "acousticness_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}


function ex05(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A5",            
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "instrumentalness_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}

function ex06(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A6",            
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "liveness_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}

function ex07(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
            title: "A7",            
            "transform": [
                {"calculate": "datum.streams / 1000000000", "as": "streams in billions"}
                ],            
            "mark": {
                "type": "point"
            },
            "encoding": {
                "y": {
                    "field": "streams in billions",
                    "type": "quantitative"
                },
                "x": {
                    "field": "speechiness_%",
                    "type": "quantitative"                    
                }
            }
        }
    };
}
```
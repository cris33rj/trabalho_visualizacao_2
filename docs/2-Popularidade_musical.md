<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>
# Parte 2 - Popularidade Musical

## Análise do que faz uma música ser popular.

Esta análise visa responder a seguinte questão: <b>Existe alguma característica que faz uma música ter mais chance de se tornar popular? </b>

Para respondê-la, geramos oito scatter plots que com o objetivo de observar a relação da variável "Streams" com "Danceability", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness" e "BMP", respectivamente. 

O gráfico que apresenta uma correlação mais forte, indicando uma característica presente em músicas populares, é que  relaciona "Stream" com "Speechiness".  O eixo Y indica a quantidade de streams em bilhões e o eixo X indica a quantidade de elementos de fala em uma música ("speechiness"). O valor mínimo zero no Eixo X refere-se a músicas com muito instrumental, sem reconhecimento claro de voz, e o valor máximo 65 é relativo a músicas cuja composição tem grande quantidade de fala humana. 

Percebe-se no gráfico que a maior parte dos pontos se concentram na parte esquerda, evidenciando que músicas com baixa "speechiness" têm um grande número de streams sendo, portanto, muito populares. À medida que a “speechiness” aumenta, há menos pontos, sugerindo que músicas com alta “speechiness” geralmente não são tão populares.

<div class="grid grid-cols-2">
    <div id="ex01" class="card">
        <h4>Danceability X Streams. A1</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex01(divWidth - 30)) }
        </div>
    </div>  
    <div id="ex02" class="card">
        <h4>Valence X Streams. A2</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex02(divWidth - 30)) }
        </div>
    </div>
    <div id="ex03" class="card">
        <h4>Energy X Streams. A3</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex03(divWidth - 30)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Acousticness X Streams. A4</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex04(divWidth - 30)) }
        </div>
    </div>
     <div id="ex05" class="card">
        <h4>Instrumentalness X Streams. A5</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex05(divWidth - 30)) }
        </div>
    </div>
    <div id="ex06" class="card">
        <h4>Liveness X Streams. A6</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex06(divWidth - 30)) }
        </div>
    </div>
     <div id="ex07" class="card">
        <h4>Speechiness X Streams. A7</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex07(divWidth - 30)) }
        </div>
    </div>
     <div id="ex08" class="card">
        <h4>BMP X Streams. A8</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex08(divWidth - 30)) }
        </div>
    </div>
</div>

```js
const divWidth = Generators.width(document.querySelector("#ex01"));

```


```js
import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";
import * as d3v6 from "npm:d3@6";



const vl = vegaLiteApi.register(vega, vegaLite);

const spotify = await FileAttachment("./data/spotify-2023.csv").csv({typed: true});


function ex01(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
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

function ex08(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: spotify
            },
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
                    "field": "bpm",
                    "type": "quantitative"                    
                }
            }
        }
    };
}
```
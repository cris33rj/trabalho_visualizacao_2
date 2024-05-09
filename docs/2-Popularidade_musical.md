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

Para respondê-la, geramos dois grupos de gráficos: 1) 7 "scatter plots" que com o objetivo de observar a relação da variável "Streams" com "Danceability", "Valence", "Energy", "Acousticness", "Instrumentalness", "Liveness", "Speechiness" e "BPM", respectivamente; 2) 7 gráficos de barras com as média percentual de cada característica musical para os artistas top 10 de todo o período analisado. 

Com relação aos "scatters plots", aqueles que apresentam uma tendência mais forte, indicando características mais frequentes em músicas populares são: "Streams X Danceability" e "Streams X Energy". O gráfico "Streams X Speechiness" apresenta também uma tendência, mas de forma inversa. 

Nos dois primeiros gráficos apontados é possível perceber que "Streams" (em bilhões) mostra uma tendência de aumento à medida que "Danceability" e "Energy" crescem, sugerindo que o público em geral aprecia mais músicas dancantes e com alto grau de energia. Quanto ao gráfico "Streams X Speechiness", percebe-se no gráfico que a maior parte dos pontos se concentram na parte esquerda, evidenciando que músicas com baixa "speechiness" (menos elementos de fala) têm um grande número de streams sendo, portanto, mais populares. Por outro lado, à medida que “speechiness” aumenta, há menos pontos, sugerindo que músicas com alta “speechiness” geralmente não são tão populares.

Quanto aos gráficos de barras, os comentários podem ser vistos mais abaixo.

<div class="grid grid-cols-2" style="width: 110%;">
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
</div>  
        <div></div>

A análise mediante os gráficos de barras permite observar, sob outro ângulo, a influência das características musicais na popularidade das músicas. Em relação ao artistas top 10 de todo o período, é possível verificar que a média de "danceability" e "energy" tem um mínimo de 50% e um máximo em torno de 80%, ao passo que as outras características tem um máximo que não passa de 65%.        

<div class="grid grid-cols-2" style="width: 110%;">         
    <div id="ex08" class="card">
        <h4>Média de "danceability" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex08(divWidth - 110)) }
        </div>
    </div>  
    <div id="ex09" class="card">
        <h4>Média de "energy" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex09(divWidth - 110)) }
        </div>
    </div>
    <div id="ex10" class="card">
        <h4>Média de "speechiness" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex10(divWidth - 110)) }
        </div>
    </div>
    <div id="ex11" class="card">
        <h4>Média de "valence" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex11(divWidth - 110)) }
        </div>
    </div>
    <div id="ex12" class="card">
        <h4>Média de "liveness" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex12(divWidth - 110)) }
        </div>
    </div>
    <div id="ex13" class="card">
        <h4>Média de "acousticness" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex13(divWidth - 110)) }
        </div>
    </div>
    <div id="ex14" class="card">
        <h4>Média de "instrumentalness" para os artistas top 10.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex14(divWidth - 110)) }
        </div>
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                      
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                      
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                      
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                      
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
                    "type": "quantitative" ,
                    "scale": {"domain": [0, 100]}                     
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                      
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
                    "type": "quantitative",
                    "scale": {"domain": [0, 100]}                     
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
                values: top_artistas_media_danceability 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B1",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex09(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_energy 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B2",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex10(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_speechiness 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B3",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex11(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_valence 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B4",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex12(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_liveness 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B5",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex13(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_acousticness 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B6",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}

function ex14(divWidth) {
    return {
        spec: {
            width: divWidth,
            data: {
                values: top_artistas_media_instrumentalness 
            },
            "transform": [{"filter": "datum.media > 0 "}],
            title: "B7",
            "mark": "bar",
            "size": 14,
            "encoding": {
                "x": {"field": "media", 
                    "type": "quantitative",
                    "axis": {
                        "labelAngle": 0  // Set the angle to 45 degrees
                    },
                    "scale": {"domain": [0, 100]}  
                },
                "y": {
                    "field": "artista", 
                    "type": "nominal",
                    "sort": {
                        "field": "media",
                        "order": "descending"
                    },                    
                }
            }            
        }
    }
}
```
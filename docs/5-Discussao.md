<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>
# 3.1 - Discussão

## Discussão dos resultados alcançados no trabalho.

Esta análise visa responder a seguinte questão:

**Discuta as diferenças entre as plataformas (Spotify, Deezer, Apple Music e Shazam)?**

Antes de discorrer sobre a questão, é necessário salientar que o o conjunto de dados, ou o DATASET analisado, conforme o próprio nome do mesmo já diz, é baseado na plataforma Spotify. Assim sendo, o comparativo fica restrito a uma quantidade menor de campos.

<div class="grid grid-cols-2">
    <div id="ext01" >
        <div>

Ante ao exposto, a primeira análise mostra que há uma concentração maior em *playlists* pertencentes a plataforma Spotify, como pode ser visto no quadro **A1**. 

O Spotify soma aproximadamente 5.000.000, enquanto que a plataforma Shazam, está ausente no conjunto de dados, mas representamos ela aqui com o nenhuma *playlist*.

Levando em consideração este conjunto de dados, infere-se que o uso de *playlist* é maior em usuários da plataforma Spotify, face a grande discrepância para o segundo colocado, e consequentemente, os demais.  

</div>
    </div>
    <div id="ex01" class="card">
        <h4>Comparativo entre o total de músicas em playlists por plataforma.</h4>
        <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex01(divWidth-160)) }
        </div>
    </div>
</div>

Já em relação aos Gráficos ("*chart*"), o cenário muda um pouco, como apresentado no diagrama **A2**: 

<div class="grid grid-cols-2">
    <div id="ex02" class="card">
        <h4>Comparativo entre o total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex02(divWidth-160)) }
        </div>
    </div>
    <div id="ext02" >
        <div>

Diferentemente do que ocorreu no quadro **A1**, a plataforma Spotify já não possui a liderança no ranqueamento, aparecendo na tímida 3° posição, somente a frente do Deezer.

O Shazam que sequer constava do DATASET para a categoria *playlist*, agora lidera, seguido de perto pela Apple.

Face ao comportamento apresentado, observa-se que um recuso ou outro é melhor usado por uma ou por outra plataforma. No caso do gráfico ("*Chart*"), o Shazam e a Apple provavelmente possuem uma melhor funcionalidade de uso para o mencionado recurso. 

</div>
    </div>
</div>

Como forma de explorar a percepção de proporção entre as plataformas para os quesitos analisados, *playlists* e *charts*, dos gráficos **A1** e **A2**, apresentamos as mesmas apurações em gráficos no formato "pizza":

<div class="grid grid-cols-2">
    <div id="ex03" class="card">
        <h4>Total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex03(divWidth-160)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Total de gráficos ("charts") por plataforma.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex04(divWidth-190)) }
        </div>
    </div>
</div>

Outros comparativos


<div class="grid grid-cols-2">
    <div id="ex05" class="card">
        <h4>Total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex05(divWidth-100)) }
        </div>
    </div>
    <div id="ex06" class="card">
        <h4>Total de gráficos ("charts") por plataforma.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex06(divWidth-300)) }
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

const spotify = await FileAttachment("./data/spotify-2023.json").json({typed: true});
showCode(FileAttachment("./comparacao_das_plataformas.csv.py"))
const comparacao_contagem_plataformas = await FileAttachment("./comparacao_das_plataformas.csv").csv({typed: true});

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
            "transform": [{"filter": "datum.Playlists != null "}],
            title: "A1",
            "mark": 
            {
                "type": "bar",
                "size": 40,
            },                
            "encoding": 
            {
                "color": {"value": "gray"},
                "x": 
                {
                   "field": ["Plataforma"],
                    "type": "nominal",                     
                    "title": "Nome da plataforma",
                    "sort": 
                    {
                        "field": "Playlists",
                        "order": "descending"
                    },
                    "axis": {"labelAngle": 45}
                },
                "y": 
                {
                   "field": ["Playlists"],
                    "aggregate": "sum",
                    "type": "quantitative",
                    "title": "Total de Playlists",
                    "scale": {"domain": [0, 5500000]}    
                },
                 "color": {"field": "Plataforma"}    
            }
        }
    }
}

function ex02(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: comparacao_contagem_plataformas
            },
            "transform": [{"filter": "datum.Charts > 0 "}],
            title: "A2",

            "mark": 
            {
                "type": "bar",
                "size": 30,
            },                
            "encoding": 
            {
                "color": {"value": "gray"},
                "x": 
                {
                   "field": ["Plataforma"],
                    "type": "nominal",                     
                    "title": "Nome da plataforma",
                    "sort": 
                    {
                        "field": "Charts",
                        "order": "descending"
                    },
                    "axis": {"labelAngle": 45}
                },
                "y": 
                {
                   "field": ["Charts"],
                    "aggregate": "sum",
                    "type": "quantitative",
                    "title": "Total de Charts",
                    "scale": {"domain": [0, 60000]}    
                },
                 "color": {"field": "Plataforma"}                    
            }
        }
    }
}

function ex03(divWidth) 
{
  return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: comparacao_contagem_plataformas
            },
            title: "A3",
            "transform": [{"filter": "datum.Playlists > 0 "}],
            "encoding": 
            {
                "theta": 
                {
                    "field": ["Playlists"], 
                    "aggregate": "sum",                                    
                    "sort": 
                    {
                        "field": ["Playlists"],
                        "type": "quantitative",
                        "order": "ascending"
                    },
                    "title": "Total de Playlists", "type": "quantitative", "stack": true,
                },
                "color": {"field": "Plataforma", "type": "nominal",  
                "sort": 
                    {
                        "field": ["Playlists"],
                        "order": "ascending"
                    },},
                "Offset": {"field": "Plataforma"},
            },
            "layer": 
            [
            {
                "mark": {"type": "arc", "outerRadius": 80, "stroke": "#fff"}
            },
            {
                "mark": {"type": "text", "radius": 100},
                "encoding": 
                {
                    "text": {"field": "Plataforma", "type": "nominal"}
                }
            }
            ]
        }
    }
}

function ex04(divWidth) 
{
  return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: comparacao_contagem_plataformas
            },
            title: "A4",
            "transform": [{"filter": "datum.Charts > 0 "}],
            "encoding": 
            {
                "theta": 
                {
                    "field": ["Charts"], 
                    "aggregate": "sum",                                    
                    "sort": 
                    {
                        "field": ["Charts"],
                        "type": "quantitative",
                        "order": "ascending"
                    },
                    "title": "Total de Charts", "type": "quantitative", "stack": true,
                },
                "color": {"field": "Plataforma", "type": "nominal",  
                "sort": 
                    {
                        "field": ["Charts"],
                        "order": "ascending"
                    },},
                "Offset": {"field": "Plataforma"},
            },
            "layer": 
            [
            {
                "mark": {"type": "arc", "outerRadius": 80, "stroke": "#fff"}
            },
            {
                "mark": {"type": "text", "radius": 100},
                "encoding": 
                {
                    "text": {"field": "Plataforma", "type": "nominal"}
                }
            }
            ]
        }
    }
}

function ex05(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: spotify
            },
            title: "A1",
            "vconcat":
            [
            {
                title: "Músicas que só aparecem na playlist do Spotify.",
                "transform": [{"filter": "datum.in_apple_playlists == 0 && datum.in_deezer_playlists == 0"}],
                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                    "value": "xxx"
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 5]}                                                 
                    },
                }
            },
            {
                title: "Músicas que só aparecem na playlist do Spotify e do Deezer.",
                "transform": [{"filter": "datum.in_apple_playlists == 0  && datum.in_deezer_playlists != 0  && datum.in_spotify_playlists != 0"}],                
                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 20]}                                                 
                    },
                }
            },
            {
                title: "Músicas que só aparecem na playlist do Spotify e do Apple.",
                "transform": [{"filter": "datum.in_apple_playlists != 0  && datum.in_deezer_playlists == 0  && datum.in_spotify_playlists != 0"}],                

                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 25]}                         
                    },
                }
            },
            {
                title: "Músicas que aparecem em todas as playlist de todas as plataformas",
                "transform": [{"filter": "datum.in_apple_playl != 0  && datum.in_deezer_playlists != 0  && datum.in_spotify_playlists != 0"}],                

                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 1000]}                         
                    },
                }
            }
            ]
        }
    }
}

function ex06(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 15,            
            data: 
            {
                values: spotify
            },
            title: "A1",
            titleLineHeight            :3,
            "vconcat":
            [
            {
                "title": "Não aparecem em chart de nenhuma plataforma",
                "transform": [{"filter": "datum.in_apple_charts == 0 && datum.in_deezer_charts == 0 && datum.in_shazam_charts == 0 && datum.in_spotify_charts == 0"}],
                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                    "value": "xxx"
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 60]}                                                 
                    },
                }
            },
            {
                title: "Ao menos uma vez nos carts de todas as plataformas.",
                "transform": [{"filter": "datum.in_apple_charts != 0 && datum.in_deezer_charts != 0 && datum.in_shazam_charts != 0 && datum.in_spotify_charts != 0"}],

                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 300]}                                                 
                    },
                }
            },
            {
                "title": "Aparecem na playlist do Spotify e do Apple." ,
                "transform": [{"filter": "datum.in_deezer_playlists == 0"}],                
                "mark": 
                {
                    "type": "bar",
                    "size": 10,
                },                
                "encoding": 
                {
                    "color": {"value": "gray"},
                    "x": 
                    {
                    "field": ["track_name"],
                        "aggregate": "count",
                        "type": "quantitative",
                        "title": "Quantidade de músicas",
                        "scale": {"domain": [0, 25]}                         
                    },
                }
            }
            ]
        }
    }
}


```

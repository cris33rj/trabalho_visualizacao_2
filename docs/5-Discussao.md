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


Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>
Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão Discussão <br>

<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>

No primeiro grupo, analisaremos os cantores:

<div class="grid grid-cols-2">
    <div id="ex01" class="card">
        <h4>Comparativo entre o total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex01(divWidth-160)) }
        </div>
    </div>
    <div id="ex02" class="card">
        <h4>Comparativo entre o total de gráficos por plataforma.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex02(divWidth-190)) }
        </div>
    </div>
</div>

<div class="grid grid-cols-2">
    <div id="ex09" class="card">
        <h4>Comparativo entre o total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex09(divWidth-160)) }
        </div>
    </div>
    <div id="ex20" class="card">
        <h4>Comparativo entre o total de gráficos por plataforma.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex09(divWidth-190)) }
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
            "transform": [{"filter": "datum.playlist > 0 "}],
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
                        "field": "Playlist",
                        "order": "descending"
                    },
                    "axis": {"labelAngle": 45}
                },
                "y": 
                {
                   "field": ["playlist"],
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
            "transform": [{"filter": "datum.charts > 0 "}],
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
                        "field": "charts",
                        "order": "descending"
                    },
                    "axis": {"labelAngle": 45}
                },
                "y": 
                {
                   "field": ["charts"],
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

function ex09(divWidth) 
{
  return {
        spec: {
            width: 300,
            padding: 15,            
            data: 
            {
                values: comparacao_contagem_plataformas
            },
            title: "A3",
            "transform": [{"filter": "datum.charts > 0 "}],
            "encoding": 
            {
                "theta": 
                {
                    "aggregate": "sum",                                    
                    "field": ["charts"], 
                    "title": "Total de Streams", "type": "quantitative", "stack": true,
                    "sort": 
                    {
                        "field": "charts",
                        "order": "descending"
                    },

                },
                "color": {"field": "Plataforma", "type": "nominal",  "legend": {"title": "Artista(s)"}},
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
```

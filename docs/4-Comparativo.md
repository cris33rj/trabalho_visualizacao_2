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

Esta seção da trabalho visa responder a terceira e última tarefa:

**Discuta as diferenças entre as plataformas (Spotify, Deezer, Apple Music e Shazam)**

Antes de discorrer sobre a tarefa, é necessário salientar que o o conjunto de dados, ou o DATASET analisado, conforme o próprio nome do mesmo já diz, é baseado na plataforma **Spotify**. Assim sendo, o comparativo fica restrito a uma quantidade menor de campos ou com dados melhor coletados para a plataforma **Spotify**.

<div class="grid grid-cols-2">
    <div id="ext01" >
        <div>

Ante ao exposto, a primeira análise mostra que há uma concentração maior em *playlists* pertencentes a plataforma **Spotify**, como pode ser visto no quadro **E1**. 

O **Spotify** soma aproximadamente 5.000.000, enquanto que a plataforma **Shazam**, está ausente no conjunto de dados. Mas, para uma melhor análise, representamos ela aqui, toda via sem nenhuma *playlist*.

Levando em consideração este conjunto de dados, infere-se que o uso de *playlist* é maior em usuários da plataforma **Spotify**, face a grande discrepância para o segundo colocado, e consequentemente, os demais.  

</div>
    </div>
    <div id="ex01" class="card">
        <h4>Comparativo entre o total de músicas em playlists por plataforma.</h4>
        <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex01(divWidth-175)) }
        </div>
    </div>
</div>

Já em relação aos *charts*, o cenário muda um pouco, como apresentado no diagrama **E2**: 

<div class="grid grid-cols-2">
    <div id="ex02" class="card">
        <h4>Comparativo entre o total de músicas em "charts" por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex02(divWidth-160)) }
        </div>
    </div>
    <div id="ext02" >
        <div>

Diferentemente do que ocorreu no quadro **E1**, a plataforma **Spotify** já não possui a liderança no ranqueamento, aparecendo na tímida 3° posição, somente a frente do **Deezer**.

O **Shazam** que sequer constava do DATASET para a categoria *playlist*, agora lidera, seguido de perto pela **Apple**.

Face ao comportamento apresentado, observa-se que um recuso ou outro é melhor usado por uma ou por outra plataforma. No caso do *Chart*, não podemos afirmar, mas presumir que as plataformas **Shazam** e **Apple** provavelmente possuem uma melhor funcionalidade de uso para o mencionado recurso. 

</div>
    </div>
</div>

Como forma de explorar a percepção de proporção entre as plataformas para os quesitos analisados, *playlists* e *charts*, dos gráficos **E1** e **E2**, apresentamos as mesmas apurações em gráficos no formato de "pizza":

<div class="grid grid-cols-2">
    <div id="ex03" class="card">
        <h4>Total de músicas em playlists por plataforma.</h4>
   <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex03(divWidth-110)) }
        </div>
    </div>
    <div id="ex04" class="card">
        <h4>Total de "charts" por plataforma.</h4>
        <div style="width: 100%; margin-top: 15px;">
            ${ vl.render(ex04(divWidth-110)) }
        </div>
    </div>
</div>

Uma outra análise comparativa feita foi sobre todas as músicas contidas no conjunto de dados e a inclusão dessas nas *playlists* das plataformas. 

Para isso, produzimos gráficos em barra que demonstrem o quantitativo de músicas que só aparecem em alguma *playlist* da plataforma **Spotify**, as músicas que pertencem a alguma *playlist* das plataformas **Spotify** e **Deezer**, mas não constam de *playlists* da **Apple**, as que fazem parte de alguma *playlist* das plataformas **Spotify** e **Apple**, mas não figuram naquelas do **Deezer** e, por fim, o quantitativo de músicas que aparecem ao menos uma vez em alguma *playlist* de todas as plataformas simultaneamente, como segue abaixo: 


<div class="grid grid-cols-1">
    <div id="ex05" class="card">
        <h4>Total de músicas em playlists por plataforma.</h4>
        <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex10(divWidth+382)) }
            ${ vl.render(ex11(divWidth+340)) }        
            ${ vl.render(ex12(divWidth+340)) }        
            ${ vl.render(ex13(divWidth+340)) }        
            ${ vl.render(ex14(divWidth+340)) }       
        </div>
    </div>
</div>

Similarmente a análise anterior, comparamos todas as músicas contidas no conjunto de dados e a inclusão dessas nas *charts* das plataformas. 

Produzimos gráficos em barra que demonstram o quantitativo de músicas que aparecem ao menos uma vez nos *charts* de todas as plataformas e um que mostra o inverso disso: as músicas que não aparecem em nenhum dos *chats* das plataformas, como segue abaixo: 

<div class="grid grid-cols-1">
    <div id="ex06" class="card">
        <h4>Total de gráficos ("charts") por plataforma.</h4>
        <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex20(divWidth+382)) }        
            ${ vl.render(ex21(divWidth+340)) }        
            ${ vl.render(ex22(divWidth+340)) }             
        </div>
    </div>
</div>

As análises poderiam ser aprofundadas, mas não vislumbramos que os demais comparativos pudessem acrescentar mais valor às análises já apresentadas. Abaixo expomos dois exemplos de outras análises: 

<div class="grid grid-cols-1">
    <div id="ex07" class="card">
        <h4>Total de charts por plataforma.</h4>
        <div style="width: 100%, margin-top: 15px;">
            ${ vl.render(ex30(divWidth+382)) }        
            ${ vl.render(ex31(divWidth+340)) }        
            ${ vl.render(ex32(divWidth+340)) }             
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
            title: "E1",
            "mark": 
            {
                "type": "bar",
                "size": 40,
            },                
            "encoding": 
            {
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
            title: "E2",

            "mark": 
            {
                "type": "bar",
                "size": 30,
            },                
            "encoding": 
            {
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
            title: "E3",
            "transform": [{"filter": "datum.Playlists != null "}],
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
                "color": {"field": "Plataforma",   
                "sort": 
                    {
                        "field": ["Playlists"],
                        "order": "descending"
                    },},
                "Offset": {"field": "Plataforma"},
            },
            "layer": 
            [
            {
                "mark": {"type": "arc", "outerRadius": 80, "stroke": "#fff"}
            },
            {
                "mark": {"type": "text", "radius": 110, "angle": {"expr" : -75},},
                "encoding": 
                {
                    "text": {"field": ["Playlists"], 
                    "format":",",
                    
                    "formatType": "number",
                    "aggregate": "sum",  
                    "type": "nominal"}
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
            title: "E4",
            "config": {"customFormatTypes": true, "formatLocale" : {   "decimal": ",", "thousands": ".", "grouping": [3], "currency": ["R$", ""] } },
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
                        "order": "descending"
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
                "mark": {"type": "text", "radius": 100,},
                "encoding": 
                {
                    "text": {"field": ["Charts"], 
                    "format":",",
                    "formatType": "number",
                    "aggregate": "sum",                                    
                    "type": "nominal",

                    }
                }
            }
            ]
        }
    }
}

function ex11(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que só aparecem nas playlists do Spotify.",
            "transform": [{"filter": "datum.in_apple_playlists == 0 && datum.in_deezer_playlists == 0"}],
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "blue"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 15]}                                                 
                },
            }
        }
    }
}
function ex12(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que só aparecem nas playlists do Spotify e do Deezer.",
            "transform": [{"filter": "datum.in_apple_playlists == 0  && datum.in_deezer_playlists != 0  && datum.in_spotify_playlists != 0"}],                
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "green"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 20]}                                                 
                },
            }
        }
    }
}

function ex13(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que só aparecem nas playlists do Spotify e do Apple.",
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
        }
    }
}

function ex14(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que aparecem em todas as playlists de todas as plataformas",
            "transform": [{"filter": "datum.in_apple_playl != 0  && datum.in_deezer_playlists != 0  && datum.in_spotify_playlists != 0"}],                
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "orange"},
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
    }
}

function ex21(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que não aparecem em ''charts'' de nenhuma plataforma.",
            "transform": [{"filter": "datum.in_apple_charts == 0 && datum.in_deezer_charts == 0 && datum.in_shazam_charts == 0 && datum.in_spotify_charts == 0"}],
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "brown"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 60]}                                                 
                },
            }
        }
    }
}

function ex22(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que aparecem ao menos uma vez nos ''charts'' de todas as plataformas.",
            "transform": [{"filter": "datum.in_apple_charts != 0 && datum.in_deezer_charts != 0 && datum.in_shazam_charts != 0 && datum.in_spotify_charts != 0"}],
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "yellow"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 300]}                                                 
                },
            }
        }
    }
}
function ex23(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que aparecem na playlist do Spotify e do Apple." ,
            "transform": [{"filter": "datum.in_deezer_playlists == 0"}],                
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "navy"},
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
    }
}

function ex31(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que aparecem ao menos uma vez em ''charts'' do  Spotify e no Shazam, mas não no Apple e do Dizzer.",
            "transform": [{"filter": "datum.in_apple_charts == 0 && datum.in_deezer_charts == 0 && datum.in_shazam_charts != 0 && datum.in_spotify_charts != 0"}],
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "silver"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 15]}                                                 
                },
            }
        }
    }
}

function ex32(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 30,            
            data: 
            {
                values: spotify
            },
            "title": "Músicas que aparecem ao menos uma vez em ''charts'' do  Spotify, mas não nos demais.",
            "transform": [{"filter": "datum.in_apple_charts == 0 && datum.in_deezer_charts == 0 && datum.in_shazam_charts == 0 && datum.in_spotify_charts != 0"}],
            "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "olive"},
                "x": 
                {
                "field": ["track_name"],
                    "aggregate": "count",
                    "type": "quantitative",
                    "title": "Quantidade de músicas",
                    "scale": {"domain": [0, 20]}                                                 
                },
            }
        }
    }
}


function ex10(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 10,            
            data: 
            {
                values: spotify
            },
            "title": "E5",
           "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "white"},
            }
        }
   }
}


function ex20(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 10,            
            data: 
            {
                values: spotify
            },
            "title": "E6",
           "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "white"},
            }
        }
   }
}

function ex30(divWidth) 
{
   return {
        spec: {
            width: divWidth,
            padding: 10,            
            data: 
            {
                values: spotify
            },
            "title": "E7",
           "mark": 
            {
                "type": "bar",
                "size": 10,
            },                
            "encoding": 
            {
                "color": {"value": "white"},
            }
        }
   }
}

```

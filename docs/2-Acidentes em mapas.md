---
toc: false
---

<style>

.hero {
  display: flex;
  flex-direction: column;
  align-items: center;
  font-family: var(--sans-serif);
  margin: 4rem 0 8rem;
  text-wrap: balance;
  text-align: center;
}

.hero h1 {
  margin: 2rem 0;
  max-width: none;
  font-size: 14vw;
  font-weight: 900;
  line-height: 1;
  background: linear-gradient(30deg, var(--theme-foreground-focus), currentColor);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero h2 {
  margin: 0;
  max-width: none;
  font-size: 3vw;
  font-style: initial;
  font-weight: 500;
  line-height: 1;
  color: var(--theme-foreground-muted);
}

@media (min-width: 640px) {
  .hero h1 {
    font-size: 90px;
  }
}

</style>

<div class="hero">
  <h2>Visualização com mapas</h2>
</div>

<div style="width: 100%; margin-top: 15px;">
    <h2 class="title">Acidentes no ano de 2023 por Estado</h2>
    <div id="ex01" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex01(divWidth01 - 80)) }
    </div>
</div>
<div style="width: 100%; margin-top: 15px;">
    <h2>EX02</h2>
    <div id="ex02" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex02(divWidth02 - 80)) }
    </div>
</div>

<div style="width: 100%; height: 500px; margin-top: 15px;">
    <h2 class="title">EX03</h2>
    <div id="ex03" style="width: 100%; height: 430px;  margin-top: 15px;">
    </div>
</div>

```js
const nycBoroughs = await FileAttachment("./data/nyc-boroughs.json").json({
  typed: true,
});
const collisions_borough = await FileAttachment(
  "./data/collisions_borough.csv"
).csv({ typed: true });

const nycNeighs = await FileAttachment("./data/nyc-neighs.json").json({
  typed: true,
});
const collisions_neighs = await FileAttachment(
  "./data/collisions_neighs.csv"
).csv({ typed: true });

const br_states = await FileAttachment("./data/br_states.json").json({
  typed: true,
});
const acidentes_por_estado = await FileAttachment(
  "./data/acidentes_por_estado.csv"
).csv({ typed: true });

const datatran2023 = await FileAttachment("./data/datatran2023.json").json({
  typed: true,
});

const brasil_completo = await FileAttachment(
  "./data/brasil_completo.json"
).json({
  typed: true,
});
```

```js
const divWidth01 = Generators.width(document.querySelector("#ex01"));
const divWidth02 = Generators.width(document.querySelector("#ex02"));
const divWidth03 = Generators.width(document.querySelector("#ex03"));
```

```js
import * as vega from "npm:vega";
import * as vegaLite from "npm:vega-lite";
import * as vegaLiteApi from "npm:vega-lite-api";

const vl = vegaLiteApi.register(vega, vegaLite);

function ex01(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 300,
      background: "#FFFFFF",
      projection: {
        type: "mercator",
      },
      layer: [
        {
          data: {
            values: br_states,
            format: {
              type: "json",
              property: "features",
            },
          },
          transform: [
            {
              lookup: "properties.Estado",
              from: {
                data: {
                  values: acidentes_por_estado,
                },
                key: "Estado",
                fields: ["Acidentes"],
              },
            },
          ],
          mark: {
            type: "geoshape",
            stroke: "#BFBFBF",
            strokeWidth: 1,
          },
          encoding: {
            color: {
              field: "Acidentes",
              type: "quantitative",
              scale: { scheme: "reds" },
            },
          },
        },
      ],
    },
  };
}

function ex02(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 300,
      background: "#FFFFFF",
      data: {
        values: datatran2023,
      },
      transform: [
        {
          calculate: "toNumber(replace(datum.latitude, ',', '.'))",
          as: "lat",
        },
        {
          calculate: "toNumber(replace(datum.longitude, ',', '.'))",
          as: "lon",
        }        
      ],
      projection: {
        type: "mercator",
      },
      layer: [
        {
          data: {
            values: br_states,
            format: {
              type: "json",
              property: "features",
            },
          },
          mark: {
            type: "geoshape",
            fill: "lightgray",
            stroke: "white",
          },
        },
        {
          mark: "circle",
          encoding: {
            longitude: { field: "lon", type: "quantitative" },
            latitude: { field: "lat", type: "quantitative" },
            size: { value: 10 },
            color: { value: "red" },
            tooltip: [
              { field: "municipio", type: "nominal", title: "Municipio" },
              { field: "causa_acidente", type: "nominal", title: "Cause" },
              { field: "tipo_acidente", type: "nominal", title: "Type" },
            ],
          },
        },
      ],
      title: "Locations of Accidents Based on Latitude and Longitude",
    },
  };
}

function ex03(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 300,
      background: "#FFFFFF",
      layer: [
        {
          data: {
            values: br_states,
            format: {
              type: "json",
              feature: "features",
            },
          },
          mark: {
            type: "geoshape",
            fill: "lightgray",
            stroke: "white",
          },
          encoding: {
            tooltip: [
              { field: "properties.name", type: "nominal", title: "State" },
            ],
          },
        },
        {
          data: {
            values: datatran2023,
            format: {
              type: "json",
            },
          },
          transform: [
            {
              calculate: "replace(datum.latitude, ',', '.')",
              as: "lat",
            },
            {
              calculate: "replace(datum.longitude, ',', '.')",
              as: "lon",
            },
          ],
          mark: "circle",
          encoding: {
            longitude: {
              field: "lon",
              type: "quantitative",
            },
            latitude: {
              field: "lat",
              type: "quantitative",
            },
            size: {
              value: 50,
            },
            color: {
              value: "red",
            },
            tooltip: [
              { field: "municipio", type: "nominal", title: "Municipio" },
              { field: "data_inversa", type: "temporal", title: "Date" },
              { field: "causa_acidente", type: "nominal", title: "Cause" },
              { field: "tipo_acidente", type: "nominal", title: "Type" },
              {
                field: "classificacao_acidente",
                type: "nominal",
                title: "Classification",
              },
              {
                field: "pessoas",
                type: "quantitative",
                title: "People Involved",
              },
              { field: "mortos", type: "quantitative", title: "Deaths" },
              {
                field: "feridos_leves",
                type: "quantitative",
                title: "Minor Injuries",
              },
              {
                field: "feridos_graves",
                type: "quantitative",
                title: "Severe Injuries",
              },
            ],
          },
        },
      ],
    },
  };
}



```

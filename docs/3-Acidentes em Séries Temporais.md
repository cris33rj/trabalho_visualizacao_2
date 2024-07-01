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
    <h2 class="title">Número de acidentes mensais no País Registrados pela PRF em 2023</h2>
    <div id="ex01" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex01(divWidth01 - 80)) }
    </div>
</div>

<div style="width: 100%; margin-top: 15px;">
    <h2 class="title">Distribuição Mensal Por Tipo de Acidente</h2>
    <h4 class="title">(Clique nos títulos das legendas ver selecionar distribuição para um tipo específico de acidente).</h4>
    <div id="ex02" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex02(divWidth02 - 80)) }
    </div>
</div>

```js
const br_states = await FileAttachment("./data/br_states.json").json({
  typed: true,
});
const datatran2023 = await FileAttachment("./data/datatran2023.json").json({
  typed: true,
});


// view(Inputs.table(datatran2023));
```

```js
const divWidth01 = Generators.width(document.querySelector("#ex01"));
const divWidth02 = Generators.width(document.querySelector("#ex02"));
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
      data: {
        values: datatran2023,
      },
      transform: [
        {
          filter: { field: "id", valid: true },
        },
        {
          filter: { field: "data_inversa", valid: true },
        },
      ],
      layer: [
        {
          params: [
            {
              name: "brush",
              select: { type: "interval", encodings: ["x"] },
            },
          ],
          mark: "area",
        },
        {
          transform: [{ filter: { param: "brush" } }],
          mark: { type: "area", color: "goldenrod" },
        },
      ],

      encoding: {
        x: {
          timeUnit: "yearmonth",
          field: "data_inversa",
          type: "temporal",
        },
        y: {
          aggregate: "count",
          field: "id",
          type: "quantitative",
          scale: {"domain": [0, 10000]}
        },
      },
    },
  };
}

function ex02(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 300,
      data: {
        values: datatran2023,
      },
      mark: {
        type: "bar",
        cornerRadiusTopLeft: 3,
        cornerRadiusTopRight: 3,
      },
      encoding: {
        x: { timeUnit: "month", field: "data_inversa", type: "ordinal" },
        y: { aggregate: "count" },
        color: {
          field: "classificacao_acidente",
          scale: {
            domain: ["Com Vítimas Fatais", "Com Vítimas Feridas", "Sem Vítimas"], // Replace with actual accident types
            range: ["#1f77b4", "#ff7f0e", "#2ca02c"], // Replace with desired colors
          },
        },
        tooltip: [
          { field: "data_inversa", title: "Date" },
          { field: "classificacao_acidente", title: "Accident Classification" },
          { aggregate: "count", title: "Count" },
        ],
      },
      selection: {
        accidentType: {
          type: "multi",
          fields: ["classificacao_acidente"],
          bind: "legend",
        },
      },
      transform: [
        { filter: { selection: "accidentType" } },
      ],
    },
  };
}

```

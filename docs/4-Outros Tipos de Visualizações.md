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
  <h2>Outros Tipos De Visualizações</h2>
</div>

<div style="width: 100%; margin-top: 15px;">
    <h2 class="title">Distribuição de Acidentes Registrados pela PRF de Acordo com o Horário</h2>
    <div id="ex01" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex01(divWidth01 - 80)) }
    </div>
</div>

<div style="width: 100%; margin-top: 15px;">
    <h2 class="title">Heatmap de Acidentes X Causas por Estado</h2>
    <div id="ex02" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex02(divWidth01 - 80)) }
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
      mark: "bar",
      encoding: {
        x: {
          field: "horario",
          type: "ordinal",
          title: "Hour of Day",
          axis: {
            labelAngle: 0,
            labelOverlap: "parity",
            labelFontSize: 12,
          },
        },
        y: {
          aggregate: "count",
          title: "Number of Accidents",
        },
        tooltip: [
          {
            field: "horario",
            type: "ordinal",
            title: "Hour of Day",
          },
          {
            aggregate: "count",
            type: "quantitative",
            title: "Number of Accidents",
          },
        ],
      },
      config: {
        axis: {
          labelFontSize: 12,
          titleFontSize: 14,
        },
        bar: {
          color: "#4c78a8",
        },
      },
    },
  };
}

function ex02(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 600,
      params: [
        {
          name: "selectedMonth",
          value: 1,
          bind: {
            input: "range",
            min: 1,
            max: 12,
            step: 1,
            name: "Mês: "
          }
        }
      ],
      data: {
        values: datatran2023,    
        
      },
      transform: [
    {
      "calculate": "toDate(datum.data_inversa + 1, '%d-%m-%Y')",
      "as": "date"
    },
    {
      "filter": "month(datum.date) == selectedMonth - 1"  // Change 1 to the desired month (1 for January, 2 for February, etc.)
    },
    {
          aggregate: [{ op: "count", as: "num_acidentes" }],
          groupby: ["uf", "tipo_acidente"],
        },
  ],   
         
      
      encoding: {
        y: { field: "uf", type: "ordinal" },
        x: {
          field: "tipo_acidente",
          type: "ordinal",
          axis: {
            labelFontSize: 12, // Increase font size of the x-axis labels
            labelAngle: 45, // Rotate x-axis labels 45 degrees
          }
        },
      },
      layer: [
        {
          mark: "rect",
          encoding: {
            color: {
              field: "num_acidentes",
              type: "quantitative",
              title: "Quantidade de Acidentes X Causa",
              legend: { direction: "horizontal", gradientLength: 120 },
            },
          },
        },
        {
          mark: "text",
          encoding: {
            text: { field: "num_acidentes", type: "quantitative" },
            color: {
              condition: { test: "datum['num_acidentes'] > 1000", value: "white" },
              value: "black",
            },
          },
        },         
      ],
      config: {
        axis: { grid: true, tickBand: "extent" },
      },
    },
  };
}

```

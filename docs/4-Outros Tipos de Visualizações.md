---
toc: false
---

<style> 
    p, li, ol, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
</style>

<div class="hero">
  <h2>Outros Tipos De Visualizações</h2>
</div>

<div style="width: 100%; margin-top: 15px;">
    <h2 style="max-width: 1500px !important; width: 1500px !important;">Distribuição de Acidentes Registrados pela PRF em 2023 de Acordo com o Horário</h2>
    <div id="ex01" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex01(divWidth01 - 80)) }
    </div>
</div>

</br>
</br>

<div style="width: 100%; margin-top: 15px;">
    <h2 style="max-width: 900px !important; width: 1000px !important;">Heatmap de Acidentes X Causas por Estado</h2>
    <div id="ex02" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex02(divWidth01 - 80)) }
    </div>
</div>
</br>
</br>

<div style="width: 100%; margin-top: 15px;">
    <h2 style="max-width: 900px !important; width: 1000px !important;">Tendências de Acidentes Registrados pela PRF entre 2021 e 2024 </h2>
    <h4 style="max-width: 900px !important; width: 1000px !important;">(Selecione o ano na barra inferior) </h4>
    <div id="ex03" style="width: 100%; margin-top: 15px;">
        ${ vl.render(ex03(divWidth01 - 80)) }
    </div>
</div>

```js
const br_states = await FileAttachment("./data/br_states.json").json({
  typed: true,
});
const datatran2023 = await FileAttachment("./data/datatran2023.json").json({
  typed: true,
});

const datatran = await FileAttachment("./data/datatran.csv").dsv({delimiter: ";",typed: true,});



// view(Inputs.table(datatran2023));
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
          name: "selectedYear",
          value: 2021,
          bind: {
            input: "range",
            min: 2021,
            max: 2024,
            step: 1,
            name: "Ano: "
          }
        },
        {
          name: "selectedMonth",
          value: 1,
          bind: {
            input: "range",
            min: 0,
            max: 12,
            step: 1,
            name: "Mês: "
          }
        }
      ],
      data: {
        values: datatran,    
        
      },
      transform: [
    {
      "calculate": "toDate(datum.data_inversa + 1, '%d-%m-%Y')",
      "as": "date"
    },
     {
          "filter": "(selectedMonth == 0 || month(datum.date) == selectedMonth - 1)"  // Allow for "all months" selection
        },
        {
          "filter": "(datum.ano == selectedYear)"  // Allow for "all years" selection
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
              condition: [{ 
                test: "datum['num_acidentes'] > 1000 && selectedMonth == 0 ", 
                value: "white" },
                { 
                test: "datum['num_acidentes'] > 70 && selectedMonth > 0 ", 
                value: "white" }],
              
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


function ex03(divWidth) {
  return {
    spec: {
      width: divWidth,
      height: 300,
      data: {
        values: datatran,
      },
      params: [
        {
          name: "selectedYear",
          value: 2021,
          bind: {
            input: "range",
            min: 2021,
            max: 2024,
            step: 1,
            name: "Ano: "
          }
        }
      ],
      transform: [
    {
      "calculate": "toDate(datum.data_inversa, '%m/%d/%Y')",
      "as": "date"
    },
    {
      "calculate": "year(datum.data_inversa)",
      "as": "year"
    },
    {
          filter: "datum.year == selectedYear"
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
          field: "date",
          type: "temporal",
        },
        y: {
          aggregate: "count",
          field: "id",
          type: "quantitative",
          scale: {"domain": [0, 2500]}
        },
      },
    },
  };
}
```

// See https://observablehq.com/framework/config for documentation.
export default {
  // The project’s title; used in the sidebar and webpage titles.
  title: "Visualização de Dados",

  // The pages and sections in the sidebar. If you don’t specify this option,
  // all pages will be listed in alphabetical order. Listing pages explicitly
  // lets you organize them into sections and have unlisted pages.
    pages: [
      {
        name: "1 - Introdução",
        open: false,
        pages: [
          {name: "1.1 - Apresentação", path: "/1-Apresentacao"},
        ]
      },
      {
        name: "2 - Desenvolvimento",
        open: false,
        pages: [
          {name: "2.1 - Acidentes em Mapas", path: "/2-Acidentes em mapas"},
          {name: "2.2 - Acidentes em Séries Temporais", path: "/3-Acidentes em Séries Temporais"},      
          {name: "2.3 - Outros Tipos de Visualizações", path: "/4-Outros Tipos de Visualizações"},          
              ]
      },
      {
        name: "3 - Fechamento",
        open: false,
        pages: [
          {name: "3.1 - Discussão", path: "/5-Discussao"},
          {name: "3.2 - Conclusão", path: "/6-Conclusao"},          
        ]
      }      
    ],

  // pages: [
  //   {
  //     name: "Examples",
  //     pages: [
  //       {name: "Dashboard", path: "/example-dashboard"},
  //       {name: "Report", path: "/example-report"}
  //     ]
  //   }
  // ],
  // Some additional configuration options and their defaults:
  theme: ["light",],  // "default", // try "light", "dark", "slate", etc.
  // header: "", // what to show in the header (HTML)
  // footer: "Built with Observable.", // what to show in the footer (HTML)
  // toc: true, // whether to show the table of contents
  // pager: true, // whether to show previous & next links in the footer
  // root: "docs", // path to the source root for preview
  // output: "dist", // path to the output root for build
  // search: true, // activate search
};

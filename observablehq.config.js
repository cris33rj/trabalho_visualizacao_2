// See https://observablehq.com/framework/config for documentation.
export default {
  // The project’s title; used in the sidebar and webpage titles.
  title: "Visualização de Dados",

  // The pages and sections in the sidebar. If you don’t specify this option,
  // all pages will be listed in alphabetical order. Listing pages explicitly
  // lets you organize them into sections and have unlisted pages.
    pages: [
      {
        name: "Introdução",
        pages: [
          {name: "Parte 1 - Apresentação", path: "/1-Apresentacao"},
        ]
      },
      {
        name: "Desenvolvimento",
        open: false,
        pages: [
          {name: "Parte 2 - Popularidade Musical", path: "/2-Popularidade_musical"},
          {name: "Parte 3 - Top 10", path: "/3-Top10"},      
          {name: "Parte 4 - Comparativo", path: "/4-Comparativo"},          
          {name: "Parte 4.1 - Comparativo teste", path: "/4-Comparativo2"},   
              ]
      },
      {
        name: "Fechamento",
        open: false,
        pages: [
          {name: "Parte 5 - Discussão", path: "/5-Discussao"},
          {name: "Parte 6 - Conclusão", path: "/6-Conclusao"},          
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
  theme: "light",  // "default", // try "light", "dark", "slate", etc.
  // header: "", // what to show in the header (HTML)
  // footer: "Built with Observable.", // what to show in the footer (HTML)
  // toc: true, // whether to show the table of contents
  // pager: true, // whether to show previous & next links in the footer
  // root: "docs", // path to the source root for preview
  // output: "dist", // path to the output root for build
  // search: true, // activate search
};

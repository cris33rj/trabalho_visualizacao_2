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

### Discussão dos resultados alcançados no trabalho.

O trabalho foi importante para aprimorar os conhecimentos nas ferramentas Observable Framework e Vega-lite, bem como o desenvolvimento em Python, com utilização de suas bibliotecas.

É importante salientar que a biblioteca D3 também é um importante componente para facilitar o desenvolvimento.

Este trabalho nos permitiu mergulhar na exploração da utilização dos gráficos, procurando encontrar neles uma melhor visualização do resultado a ser mostrado de forma inteligível ao leitor.

Buscamos a cada tópico explicar nossas escolhas pelos gráficos, como eles poderiam auxiliar a explicar o resultado de nossas análises e, ainda, como realça-las, tendo em vista que alguns tipos de gráficos podem mostrar um mesmo resulta, entretanto, alguns tendem a melhorar a percepção do leitor em algumas situações. 

A escolha do DATASET para este trabalho foi motivada por alguns critérios: 
1.	Deveria ser pública e acessível a todos;
2.	Deveria ser preferencialmente disponibilizada pelo governo brasileiro;
3.	Deveria se referir a algum problema ocorrido no território brasileiro;
4.	Deveria possibilitar um comparativo temporal;
5.	Deveria nos permitir explorar os conhecimentos obtidos sobre visualização projetada sobre mapas; e
6.	Deveria possuir uma quantidade razoável de campos e dados.

Optamos, então, por um conjunto de dados contendo ocorrências em vias federais fiscalizadas pela Polícia Rodoviária Federal. A base de dados é rica em documentar várias informações sobre a ocorrência de acidentes nessas vias e possuía registro de vários anos, dos quais optamos por 4: 2021, 2022, 2023 e 2024, tendo este último, informações até o dia 17 de maio.

De posse dessas informações, debruçamo-nos a responder às seguintes questões:

1.	Há uma maior ou menor tendência a ocorrência de acidentes em determinado mês do ano?
2.	Quais estados concentram a maior taxa de acidentes?
3.	Há uma relação entre tamanho do estado e a quantidade de acidentes?
4.	Há uma região ou município específico onde certos tidos de acidentes ocorrem com maior frequência?
5.	Quais tipos de acidentes são mais relevantes por estado?
6.	A quantidade total de acidentes, incluindo todas as classificações, varia entre os anos?
7.	Entre as classificações de gravidade houve alguma que variou substancialmente entre os anos?
8.	Quais tipos e causas de infração são as mais comuns?
9.	Há variações nas infrações mais comuns por estado ou por ano?
10.	Considerando que a maior parte do trânsito ocorre em condições de boa visibilidade, é correto afirmar que a maioria dos acidentes também acontece nessas circunstâncias?
11.	Considerando que em períodos de chuva a ocorrência de aquaplanagem, derrapagens, enchentes, deslizamentos de terra e outros eventos aumentam significativamente, em que posição o clima chuvoso se encontra em relação ao total de acidentes ocorridos entre 2021 e 2024 em estradas federais, segundo os registros da Polícia Rodoviária Federal?
12.	Sendo um país tropical, onde as temperaturas são predominantemente mais altas e não favorecem a formação de neve, há algum registro de acidente automobilístico ocorrido sob condições de neve?
13.	Em qual período do dia há a incidência do maior e menor número de acidentes?

Passando a análise, apuramos que há uma tendência de estabilidade na ocorrência de acidente durante o ano, com uma leve discrepância de alta para o mês de março e baixa para o mês de abril, provavelmente influenciados por fatores econômicos e sociais. No quesito estado com maior número de acidentes, Minas Gerais ganha destaque, uma vez que possui a maior malha viária do país, repetindo as posições no ranking a cada anos para todos os estados.

Em relação a questão envolvendo gravidade em acidentes, o ano de 2003 ganha relevo frente aos demais, tomando-se como medida a ocorrência de fatalidades, 150 registradas, em comparação a 2021 que se salienta em relação a pessoas feridas.

Sob a ótica, a de análise das causas, não se nota um padrão, nem em relação ao estado, nem em relação ao ano, o que não nos permite uma melhor conclusão a não ser aleatoriedade do fato. Já em relação ao tipo, colisão na traseira, saída de leito carroçável e colisão transversal ocorrem seguidamente nesta ordem para todos os anos analisado, diferentemente das causas, podendo ser previsível a ordem da quantidade de ocorrências.

As últimas foram direcionadas a certificarem ou não algumas premissas lógicas. Confirmou duas delas, a que considera que a maior parte do trânsito ocorre em condições de boa visibilidade e, por isto, a maioria dos acidentes também aconteceriam nessas mesmas circunstâncias, e a que a maior parte dos acidentes ocorre durante o final de semana: sábado e domingo. Contudo, a análise não validou aprespectiva de que chuva, com seus demais desdobramentos, seria o maior causador de acidentes em caso de má visibilidade, pois apurou-se que o clima nublado é o que ocupa tal posição. Na mesma linha observou-se que muito embora o Brasil seja um país tipicamente tropical, é possível encontrar registros de acidentes tendo como clima a neve.

```

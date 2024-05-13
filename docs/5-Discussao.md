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

O trabalho foi importante para aprimorar os conhecimentos nas ferramentas Observable Framework e Vega-lite, bem como o desenvolvimento em Python, com utilização de suas bibliotecas.

É importante salientar que a biblioteca D3 também é um importante componente para facilitar o desenvolvimento.

Este trabalho nos permitiu mergulhar na exploração da utilização dos gráficos, procurando encontrar neles uma melhor visualização do resultado a ser mostrado de forma inteligível ao leitor.

Buscamos a cada tópico explicar nossas escolhas pelos gráficos, como eles poderiam auxiliar a explicar o resultado de nossas análises e, ainda, como realça-las, tendo em vista que alguns tipos de gráficos podem mostrar um mesmo resulta, entretanto, alguns tendem a melhorar a percepção do leitor em algumas situações. 

Convem destacar que o DATASET utilizado, aparentemente, tem como base principal a plataforma **Spotify**, o que pode representar alguma divergência na comparação com as demais plataformas. Adicionalmente, vale lembrar que alguns campos também são focados em dados obtidos na plataforma **Spotify**, como é o caso do *Streams*, um dos campos que mais usamos em nossas análises e que, a princípio, não serve de ancoragem para as demais plataformas.

Passando a análise, como vimos no item 2.1, Popularidade musical, não há uma afirmação irrefutável sobre um determinado item ou outro que, se satisfeito, fazem com que um determinada música seja um sucesso. Mas há indícios, como vimos, nos gráficos de dispersão (A1 a A5) que, pela concentração de pontos demonstradas nos gráficos, presume-se que "danceability" e "energy" são características a serem buscadas para atingimento do sucesso musical, tendo em vista sua prevalência em músicas de maior sucesso. Tal conclusão é reforçada pelos gráficos de barras (B1 a B4) que exibem uma maior média de "danceability" e "energy" nas músicas dos artistas top 10 de todo o período analisado.  

Já no item 2.2, Top 10, verificamos que há uma variação tanto do *ranking* de artistas quanto de músicas mais ouvidas quando se considera todas as músicas independente do ano de lançamento frente àquelas lançadas em um determinado ano. Isto se dá justamente pelo lançamento ou não de novas músicas que caem ou não no gosto musical da população.

Por fim, no item 2.3, Comparativo, observa-se que um recuso ou outro é melhor usado por uma ou por outra plataforma. No caso do gráfico ("*Chart*"), não podemos afirmar, mas presumir que as plataformas **Shazam** e **Apple** provavelmente possuem uma melhor funcionalidade de uso para o mencionado recurso, o mesmo ocorrendo com a *playlist*, no caso do **Spotify**, plataforma base para a obtenção do DATASET. 


```

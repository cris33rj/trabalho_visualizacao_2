<style> 
    p, table, figure, figcaption, h1, h2, h3, h4, h5, h6, .katex-display 
    {
        max-width:none;
        text-align: justify;
        margin: 15px 15px;
        text-wrap: pretty;
    }
    li,ul,ol
    {
        text-align: justify;
        max-width:none;
        text-wrap: pretty;
    }
</style>

# 1.1 - Apresentação

### O trabalho:

Este trabalho de pesquisa foi produzido no curso de Mestrado em Computação - PGC UFF, como atividade parcial para cumprimento da disciplina de **VISUALIZAÇÃO DE DADOS** (SI & PGC - UFF), ministrado pelo Professor **Marcos Lage**.

### Os alunos:

<div class="grid grid-cols-1">    
<div class="card" >

| Edel Melo          | Cristiano Nascimento          |
| :----:             |    :----:           |
| Aluno de Mestrado <BR> Mat. M048.123.012  | Aluno de Mestrado <br> Mat. M048.123.010  |
| <address><a href="mailto:edelmelo@id.uff.br">edelmelo@id.uff.br</a></address> | <address><a href="mailto:cristiano_nascimento@id.uff.br">mailto:cristiano_nascimento@id.uff.br</a></address> |

</div>
</div>

### A tarefa:

 O foco desse trabalho é investigar, com base nos dados de ocorrências de trânsito fornecidos pela Polícia Rodoviária Federal, os fatores que mais contribuíram para o número de acidentes nas estradas federais. Além disso, busca-se evidenciar as relações existentes e, muitas vezes, não percebidas, no que diz respeito à composição dos diferentes tipos de agrupamentos.

### O software:

Para desenvolvimento do trabalho, deveríamos utilizar:
1. Observable Framework;
2. Biblioteca do D3;
3. Vega-lite;
4. Python;
5. Node.js; e
6. Bibliotecas diversas do python (Numpy, Pandas, Matplotlib, Seaborn, Itertools e sys);

### A base de dados:

Para realização da tarefa foi utilizado conjunto de dados ofertados através de bases públicas como descrito aseguir:

Arquivos: Datatran2021.csv, Datatran2022.csv, Datatran2023.csv e Datatran2024.csv<br>
Local de origem: https://www.gov.br/prf/pt-br/acesso-a-informacao/dados-abertos/dados-abertos-da-prf<br>
Descrição: Dados de acidentes coletados pela PRF.

Dicionário de dados:
<div class="grid grid-cols-1">    
<div class="card" >

| Ordem          | Campo          | Descrição |
| :----:             |    :----:           |    :----           |
|	1	|	id 	|	Variável com valores numéricos,representando o identificador do acidente.	|
|	2	|	data_inversa 	|	Data da ocorrência no formatodd/mm/aaaa.	|
|	3	|	dia_semana	|	Dia da semana da ocorrência. Ex.:Segunda, Terça, etc.	|
|	4	|	horário	|	Horário da ocorrência no formatohh:mm:ss.	|
|	5	|	uf	|	Unidade da Federação. Ex.: MG, PE, DF,etc.	|
|	6	|	br	|	Variável com valores numéricos,representando o identificador da BR do acidente.ponto.	|
|	7	|	km 	|	Identificação do quilômetro onde ocorreu o acidente, com valor mínimo de 0,1 km ecom a casa decimal separada por 	|
|	8	|	municipio	|	Nome do município de ocorrência do acidente.	|
|	9	|	causa_acidente	|	Identificação da causa principal doacidente. Neste conjunto de dados são excluídos os acidentes com a variávelcausa principal igual a “Não”.	|
|	10	|	Tipo_acidente	|	Identificação do tipo de acidente. Ex.:Colisão frontal, Saída de pista, etc. Neste conjunto de dados são excluídos os tiposde acidentes com ordem maior ou igual a dois. A ordem do acidente na acidente: Sem Vítimas, Com VítimasFeridas, Com Vítimas Fatais e Ignorado.mesma ocorrência.	|
|	11	|	classificação_acidente	|	Classificação quanto à gravidade do demonstra asequência cronológica dos tipos presentes 	|
|	12	|	fase_dia	|	Fase do dia no momento do acidente. Ex.Amanhecer, Pleno dia, etc.	|
|	13	|	sentido_via	|	Sentido da via considerando o ponto decolisão: Crescente e decrescente.	|
|	14	|	condição_meteorologica	|	Condição meteorológica no momento doacidente: Céu claro, chuva, vento, etc.	|
|	15	|	tipo_pista	|	Tipo da pista considerandoa quantidade de faixas: Dupla, simples ou múltipla.	|
|	16	|	tracado_via	|	Descrição do traçado da via.	|
|	17	|	uso_solo	|	Descrição sobre as características do localdo acidente: Urbano=Sim;Rural=Não.	|
|	18	|	pessoas	|	Total de pessoas envolvidas na ocorrência.	|
|	19	|	mortos	|	Total de pessoas mortas envolvidas naocorrência.	|
|	20	|	feridos_leves	|	Total de pessoas com ferimentos levesenvolvidas na ocorrência.	|
|	21	|	feridos_graves	|	Total de pessoas com ferimentos gravesenvolvidas na ocorrência.	|
|	22	|	ilesos	|	Total de pessoas ilesas envolvidas naocorrência.	|
|	23	|	ignorados 	|	Total de pessoas envolvidas na ocorrência e que não se soube o estado físico.veículos envolvidos na 	|
|	24	|	feridos	|	Total de pessoas feridas envolvidas na ocorrência (éa soma dos feridos leves com os graves).	|
|	25	|	veiculos	|	Total de ocorrência.	|
|	26	|	latitude	|	Latitude do local do acidente em formato geodésico decimal.	|
|	27	|	longitude	|	Longitude do local do acidente em formato geodésico decimal.	|
|	28	|	regional	|	Superintendência regional da PRF cujo acidente ocorreu dentro dos limites de suacircunscrição . Atenção nem semprea UF da regional coincide com a UF doacidente. Ex:A circunscrição da SPRF-DF “GO”.grande parte está localizada na UF	|
|	29	|	delegacia	|	delegacia da PRF cujo acidente ocorreu dentro dos limites de sua circunscrição.	|
|	30	|	uop	|	UOP é unidade operacional. Unidade operacional da PRF cujo acidente ocorreudentro dos limites de sua circunscrição.	|
</div>
</div>
<h6>Ref.:  https://drive.google.com/file/d/11pXLw_0D0hHVS8fiC8cv2dPX39vpuOH1/view</h6>

Arquivo: br_stats.json<br>
Local de origem: https://www.ibge.gov.br/geociencias/organizacao-do-territorio/malhas-territoriais/15774-malhas.html?=&t=downloads<br>
Descrição: Polígonos de mapa para dados de municípios.

Arquivo: brasil_completo.json<br>
Local de origem: https://github.com/adolfoguimaraes/mapas_dataset/blob/main/brasil/BR_Municipios_2020_small.json<br>
Descrição: Polígonos de mapa para dados de municípios.

Arquivo: br_states.json<br>
Local de origem: https://github.com/giuliano-macedo/geodata-br-states/blob/main/geojson/br_states.json<br>
Descrição: Polígonos de mapa para dados dos estados.

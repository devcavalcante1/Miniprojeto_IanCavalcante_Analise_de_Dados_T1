**Curso:** SENAI Carreira Tech — Trilha Análise de Dados  
**Turma:** Analise_de_Dados_T1  
**Aluno:** Ian Cavalcante  
**Linguagem:** Python  
**Biblioteca principal:** Pandas

## 1. Sobre o projeto

Este projeto tem como objetivo realizar uma Análise Exploratória de Dados (EDA — *Exploratory Data Analysis*) sobre uma base de dados de varejo, utilizando Python e Pandas.

A análise busca compreender a estrutura dos dados, identificar problemas de qualidade, realizar o tratamento inicial da base, calcular estatísticas descritivas e investigar padrões relacionados a clientes, produtos e categorias.

O projeto faz parte das atividades práticas de análise de dados do SENAI Carreira Tech.

## 2. Objetivos

- Carregar e explorar uma base de dados em formato CSV.
- Identificar a quantidade de registros, colunas e os tipos de dados.
- Investigar valores ausentes e colunas sem informação.
- Converter a coluna de datas para o formato adequado.
- Identificar e avaliar registros duplicados.
- Calcular estatísticas descritivas da variável `CL_FHL`.
- Analisar registros por clientes, produtos, categorias e gênero.
- Extrair insights a partir dos resultados obtidos.
- Documentar as decisões de tratamento e as limitações da análise.

## 3. Tecnologias utilizadas

| Tecnologia | Aplicação |
|---|---|
| Python 3.10 | Linguagem de programação |
| Pandas | Manipulação, limpeza e análise dos dados |
| VS Code | Ambiente de desenvolvimento |
| Git | Controle de versão |
| GitHub | Hospedagem e compartilhamento do projeto |

## 4. Estrutura dos dados

O arquivo de entrada utilizado é `Varejo.csv`.

A base original contém **830.000 registros e 14 colunas**. Após a remoção das quatro colunas totalmente vazias, restam 10 colunas úteis.

| Coluna | Descrição adotada no projeto |
|---|---|
| `DATA` | Data do registro |
| `CO_ID` | Identificador da compra ou operação |
| `CL_ID` | Identificador do cliente |
| `CL_GENERO` | Gênero cadastrado do cliente |
| `CL_EC` | Código de estado civil |
| `CL_FHL` | Quantidade de filhos informada |
| `CL_SEG` | Código de segmento do cliente |
| `PR_ID` | Identificador do produto |
| `PR_CAT` | Categoria do produto |
| `PR_NOME` | Nome do produto |

**Observação:** as descrições das colunas representam a interpretação adotada na análise. Para confirmar o significado de todos os códigos categóricos, é necessário consultar o dicionário de dados da fonte original.

## 5. Etapas do projeto

### 5.1. Carregamento e exploração

A base foi carregada com `pandas.read_csv()`, utilizando o ponto e vírgula como separador.

Foram examinados:

- Dimensões da base por meio de `shape`.
- Nomes das colunas por meio de `columns`.
- Tipos de dados por meio de `dtypes`.
- Estrutura e valores preenchidos por meio de `info()`.
- Amostras dos registros por meio de `head()`.

### 5.2. Limpeza e tratamento

As seguintes verificações e transformações foram realizadas:

- Identificação de quatro colunas totalmente vazias.
- Remoção dessas colunas, reduzindo a base de 14 para 10 colunas.
- Conversão da coluna `DATA` para o tipo `datetime64[ns]`.
- Verificação de datas ausentes ou inválidas.
- Verificação de valores ausentes nas colunas restantes.
- Investigação de duplicatas exatas.
- Identificação de registros com a categoria `#N/D`.

Após a limpeza inicial, não foram encontrados valores ausentes nas 10 colunas restantes, e a conversão das datas não gerou valores inválidos.

### 5.3. Investigação de duplicatas

Foram identificadas **96.553 linhas duplicadas exatas**, correspondentes a aproximadamente 11,63% das 830.000 linhas.

A operação `drop_duplicates()` foi utilizada para comparar a dimensão da base antes e depois da remoção dessas repetições.

| Indicador | Resultado |
|---|---:|
| Linhas antes da deduplicação | 830.000 |
| Linhas após a deduplicação | 733.447 |
| Linhas identificadas como duplicadas | 96.553 |
| Percentual de duplicatas | 11,63% |

**Limitação:** a identificação de linhas duplicadas não comprova, por si só, que elas sejam erros. Como não foi identificado um identificador único de cada item vendido, a exclusão definitiva deve depender da validação da regra de negócio. Por esse motivo, os resultados exploratórios apresentados neste documento são referentes à base após a remoção das colunas vazias, mas antes da exclusão das duplicatas.

### 5.4. Exploração de clientes e produtos

Foram calculadas as quantidades de identificadores distintos e os rankings de registros por cliente e produto.

Resultados encontrados:

- **18.471** valores distintos em `CO_ID`.
- **1.000** clientes distintos em `CL_ID`.
- **229** produtos distintos em `PR_ID`.

Também foram analisados os clientes com maior quantidade de registros, os produtos mais frequentes e a distribuição das linhas por categoria.

### 5.5. Estatística descritiva

A variável `CL_FHL` foi analisada utilizando média, mediana, moda, desvio padrão, mínimo, máximo, contagem e quartis.

| Estatística | Resultado |
|---|---:|
| Valores válidos | 830.000 |
| Média | 1,1465 |
| Mediana | 0 |
| Moda | 0 |
| Desvio padrão amostral | 1,4170 |
| Mínimo | 0 |
| Máximo | 4 |
| Primeiro quartil (25%) | 0 |
| Segundo quartil (50%) | 0 |
| Terceiro quartil (75%) | 2 |

A análise foi inicialmente calculada sobre as linhas da base. Como cada cliente pode aparecer em vários registros, essas estatísticas não devem ser interpretadas como uma distribuição por cliente único.

### 5.6. Agrupamentos com Pandas

Foram utilizados `groupby()`, `size()`, `nunique()` e `agg()` para analisar os dados sob diferentes perspectivas.

As análises incluem:

- Quantidade de registros por categoria de produto.
- Quantidade de registros e clientes distintos por gênero.
- Média de `CL_FHL` por gênero.
- Produtos com maior quantidade de registros.
- Clientes com maior quantidade de registros.

## 6. Principais resultados e insights

### 6.1. Distribuição por categoria

A categoria ALIMENTOS apresentou a maior quantidade de registros, seguida por HIGIENE e LIMPEZA.

| Categoria | Registros |
|---|---:|
| ALIMENTOS | 434.767 |
| HIGIENE | 155.574 |
| LIMPEZA | 145.754 |
| BEBIDAS | 43.299 |
| PET | 32.399 |
| ACESSORIOS | 14.557 |
| `#N/D` | 3.650 |

ALIMENTOS representa aproximadamente 52,38% das linhas analisadas.

### 6.2. Perfil por gênero

| Gênero | Registros | Clientes distintos | Média de `CL_FHL` por registro |
|---|---:|---:|---:|
| F | 432.576 | 519 | 1,0907 |
| M | 397.424 | 481 | 1,2074 |

O gênero F concentra aproximadamente 52,12% dos registros. Essa diferença representa a distribuição das linhas da base e não permite concluir qual grupo possui maior gasto ou faturamento.

### 6.3. Produtos frequentes

Entre os produtos com maior quantidade de registros por nome estão:

- PRESUNTO COZIDO — 14.381 registros.
- SARDINHA — 7.490 registros.
- GEL — 7.399 registros.
- BANANA — 7.385 registros.
- DESENGORDURANTE — 7.378 registros.

Essas contagens representam a frequência dos registros na base, e não necessariamente a quantidade de unidades vendidas.

### 6.4. Qualidade e classificação

A base contém 3.650 registros com `PR_CAT` igual a `#N/D`. Esse valor textual indica uma categoria não identificada ou não classificada, que pode exigir investigação adicional.

Além disso, a presença de 96.553 duplicatas exatas representa um ponto importante de atenção na avaliação da qualidade dos dados.

### 6.5. Distribuição da quantidade de filhos

A variável `CL_FHL` apresenta média de aproximadamente 1,15, mediana igual a zero e moda igual a zero quando calculada sobre os registros.

Esses resultados sugerem uma concentração de linhas associadas a clientes com zero filhos informados. Uma análise por cliente único é necessária para descrever adequadamente o perfil cadastral.

## 7. Como executar o projeto

### Pré-requisitos

- Python 3.10 ou versão compatível.
- Git instalado.
- Visual Studio Code ou outro editor Python.
- Arquivo `Varejo.csv` disponibilizado no diretório `data/`.

### Clonar o repositório

Substitua a URL abaixo pelo endereço do repositório publicado no GitHub.

```bash
git clone URL_DO_SEU_REPOSITORIO
cd Miniprojeto_IanCavalcante_Analise_de_Dados_T1
```

### Criar e ativar o ambiente virtual

No macOS ou Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### Instalar as dependências

Se o arquivo `requirements.txt` estiver disponível:

```bash
pip install -r requirements.txt
```

Caso ele ainda não exista, instale o Pandas:

```bash
pip install pandas
```

### Executar a análise

```bash
python -u src/analise_varejo.py
```

O comando `-u` permite que as mensagens de saída sejam exibidas sem o buffer habitual, facilitando o acompanhamento da execução.

## 8. Estrutura sugerida do repositório

```text
Miniprojeto_IanCavalcante_Analise_de_Dados_T1/
│
├── data/
│   ├── Varejo.csv
│   └── Varejo_limpo.csv
│
├── src/
│   └── analise_varejo.py
│
├── README.md
├── README_NomeDoAluno_Turma.md
├── requirements.txt
└── .gitignore
```

O arquivo `Varejo_limpo.csv` deve ser incluído após a implementação e validação da etapa de exportação da base tratada. A estrutura acima é uma sugestão de organização; os arquivos devem corresponder ao que efetivamente existe no repositório.

## 9. Limitações da análise

- A base não apresenta uma coluna explícita de preço ou valor de venda, impossibilitando análises de faturamento.
- A quantidade de registros não equivale necessariamente à quantidade de unidades vendidas.
- As duplicatas exatas precisam de validação antes de uma exclusão definitiva.
- A categoria `#N/D` permanece como pendência de classificação.
- A interpretação de códigos como `CL_EC` e `CL_SEG` depende de um dicionário de dados.
- As estatísticas calculadas sobre registros podem diferir das estatísticas calculadas sobre clientes únicos.

## 10. Conclusão

O projeto permitiu aplicar conceitos fundamentais de análise de dados com Python e Pandas, incluindo exploração, limpeza, validação, estatística descritiva e agrupamento.

A análise identificou colunas sem informação, confirmou a conversão das datas, investigou duplicatas e revelou a distribuição dos registros entre categorias, clientes e produtos.

Os resultados demonstram a importância de avaliar a qualidade dos dados e de documentar as limitações antes de produzir conclusões. Como próximos passos, recomenda-se validar a regra de deduplicação, investigar as categorias não classificadas, gerar e verificar a base final tratada e consolidar as análises por cliente único.

# Relatório de Análise de Dados de Varejo --- Power BI

**Projeto acadêmico:** SENAI Carreira Tech --- Trilha Análise de Dados\
**Base analisada:** `Varejo.csv`\
**Resultados de referência:** execução do projeto Python/Pandas
compartilhada na conversa.

## O que acompanha este pacote

-   `dados_resumidos/`: tabelas CSV com os resultados agregados já
    conhecidos.
-   `medidas_DAX_sugeridas.txt`: medidas para quando a base original for
    importada no Power BI.
-   `dashboard_preview.html`: protótipo interativo local, baseado
    exclusivamente nos agregados conhecidos.

## Limitação importante

Este pacote **não é um arquivo `.pbix` nativo**. O arquivo original
`Varejo.csv` não foi disponibilizado como arquivo acessível nesta etapa;
só estão disponíveis os resultados agregados da análise. Portanto, não
foram inventadas linhas transacionais. Os CSVs aqui são tabelas-resumo,
adequadas para reproduzir gráficos agregados, mas não substituem a base
detalhada para filtros cruzados completos.

Para construir o relatório nativo: 1. Abra o Power BI Desktop. 2.
Selecione **Obter dados \> Texto/CSV** e importe a base original
`Varejo.csv`. 3. Confira o separador `;` e converta `DATA` para tipo
Data, interpretando dia antes do mês. 4. Remova as colunas totalmente
vazias `Unnamed: 10` até `Unnamed: 13`. 5. Não exclua duplicatas sem
validar a chave de negócio. As 96.553 linhas idênticas são uma pendência
de investigação, não prova automática de erro. 6. Crie as medidas em
`medidas_DAX_sugeridas.txt`. 7. Monte as páginas conforme a proposta
abaixo.

## Proposta de páginas

### 1. Visão geral

-   Cartões: 830.000 registros; 1.000 clientes distintos; 229 produtos
    distintos; 18.471 valores distintos de `CO_ID`.
-   Gráfico de barras: registros por categoria.
-   Nota: `CO_ID` foi tratado apenas como identificador distinto nos
    resultados disponíveis; confirmar se representa uma compra, pedido,
    cupom ou outra entidade.

### 2. Produtos e categorias

-   Barras: registros por categoria.
-   Barras horizontais: top 10 combinações `PR_ID` + `PR_NOME` por
    frequência.
-   Não chamar frequência de vendas em unidades ou faturamento sem
    confirmar a semântica da base.

### 3. Perfil dos clientes

-   Registros por `CL_GENERO`.
-   Distribuição de `CL_FHL` por número de filhos.
-   Clientes distintos por gênero.
-   A média de filhos fornecida na análise inicial é ponderada por
    registros, não calculada uma única vez por cliente. Para análise
    demográfica, deduplicar por `CL_ID` após validar consistência dos
    atributos.

### 4. Qualidade dos dados

-   Quatro colunas inteiramente vazias removidas.
-   Zero datas inválidas após conversão.
-   Zero nulos nas dez colunas úteis após limpeza.
-   96.553 duplicatas exatas detectadas (11,63% dos registros
    originais).
-   3.650 registros com categoria `#N/D`.

## Resultados conhecidos

-   Categorias: ALIMENTOS 434.767; HIGIENE 155.574; LIMPEZA 145.754;
    BEBIDAS 43.299; PET 32.399; ACESSORIOS 14.557; `#N/D` 3.650.
-   Top produtos por frequência: ÁGUA SANITÁRIA (ID 93, 3.773);
    DESENGORDURANTE (ID 98, 3.760); LEITE (ID 37, 3.757); SARDINHA (ID
    61, 3.746); SARDINHA (ID 129, 3.744).
-   `CL_FHL` por registro: 0 filhos 435.501; 1 filho 102.813; 2 filhos
    106.622; 3 filhos 104.685; 4 filhos 80.379.
-   Gênero: F 432.576 registros e 519 clientes distintos; M 397.424
    registros e 481 clientes distintos.

## Validações pendentes antes da apresentação final

-   Confirmar a definição de `CO_ID` e se cada linha representa um item
    de uma compra ou outro evento.
-   Confirmar por que existem 96.553 linhas duplicadas exatas e qual é a
    chave única correta.
-   Verificar o significado de `CL_EC`, `CL_SEG` e dos valores
    codificados.
-   Investigar os 3.650 registros de categoria `#N/D`.
-   Importar a base original no Power BI para habilitar filtros
    dinâmicos por data, cliente, produto e categoria.
-   Não apresentar faturamento, receita, ticket médio ou quantidade
    vendida: esses campos não aparecem na estrutura conhecida da base.


from pathlib import Path

import pandas as pd

# 1. Identifica a pasta principal do projeto.
PASTA_PROJETO = Path(__file__).resolve().parent.parent

# 2. Define o caminho do arquivo CSV.
CAMINHO_CSV = PASTA_PROJETO / "data" / "Varejo.csv"

# 3. Verifica se o arquivo existe.
if not CAMINHO_CSV.exists():
    raise FileNotFoundError(
        f"Arquivo não encontrado: {CAMINHO_CSV}"
    )

# 4. Carrega a base de dados.
df = pd.read_csv(
    CAMINHO_CSV,
    sep=";"

)

print("Etapa 1: iniciando leitura do CSV...", flush=True)
# código de leitura

# 5. Apresenta informações iniciais.
print("\n=== ANÁLISE EXPLORATÓRIA DE DADOS ===")

print("\n1. Dimensões da base:")
print(f"Quantidade de registros: {df.shape[0]}")
print(f"Quantidade de colunas: {df.shape[1]}")

print("\n2. Nomes das colunas:")
print(df.columns.tolist())

print("\n3. Tipos de dados:")
print(df.dtypes)

print("\n4. Primeiras cinco linhas:")
print(df.head())

print("\n5. Informações gerais:")
df.info()

print("\n=== VERIFICAÇÃO DO CABEÇALHO ===")
print(df.columns.tolist())

print("\n=== VALORES NULOS POR COLUNA ===")
print(df.isnull().sum())

print("\n=== AMOSTRA DOS DADOS ===")
print(df.head(3).to_string())


# ==================================================
# SPRINT 2 - LIMPEZA E DIAGNOSTICO DOS DADOS
# ==================================================

print("Etapa 2: leitura concluída.", flush=True)
# código de limpeza

print("\n=== SPRINT 2: LIMPEZA DOS DADOS ===")

# 1. Registrar o tamanho original da base.
print(f"Dimensoes originais: {df.shape}")

# 2. Remover colunas totalmente vazias.
colunas_vazias = df.columns[df.isna().all()].tolist()

print("\nColunas totalmente vazias:")
print(colunas_vazias)

df = df.drop(columns=colunas_vazias)

print(f"Dimensoes apos remover colunas vazias: {df.shape}")

# 3. Remover espacos desnecessarios dos textos.
colunas_texto = df.select_dtypes(include="object").columns

for coluna in colunas_texto:
    df[coluna] = df[coluna].str.strip()

# 4. Converter textos vazios em valores ausentes.
for coluna in colunas_texto:
    df[coluna] = df[coluna].replace("", pd.NA)

# 5. Converter DATA para datetime.
df["DATA"] = pd.to_datetime(
    df["DATA"],
    format="%d/%m/%Y",
    errors="coerce"
)

# 6. Investigar datas que nao puderam ser convertidas.
datas_invalidas = df["DATA"].isna().sum()

print(f"\nDatas ausentes ou invalidas: {datas_invalidas}")

# 7. Verificar valores ausentes por coluna.
print("\nValores ausentes por coluna:")
print(df.isna().sum())

# 8. Verificar linhas totalmente duplicadas.
duplicatas = df.duplicated().sum()

print(f"\nLinhas totalmente duplicadas: {duplicatas}")

# 9. Verificar categorias vazias.
for coluna in ["CL_GENERO", "CL_SEG", "PR_CAT", "PR_NOME"]:
    if coluna in df.columns:
        vazios = df[coluna].isna().sum()
        print(f"Valores ausentes em {coluna}: {vazios}")

# 10. Conferir os tipos de dados apos a limpeza.
print("\nTipos de dados apos a limpeza:")
print(df.dtypes)

print("\nAmostra da base:")
print(df.head(3).to_string(index=False))



# ==================================================
# SPRINT 3 - INVESTIGACAO DE DUPLICATAS
# ==================================================
print("\nInvestigando duplicatas...")


print("Etapa 3: iniciando análise de duplicatas...", flush=True)
# código de investigação de duplicatas

mascara_duplicadas = df.duplicated()

print("Investigação concluída.")
print("Linhas duplicadas:", mascara_duplicadas.sum())

# Mostrar apenas 10 exemplos, sem ordenar todas as duplicatas
exemplos = df.loc[mascara_duplicadas].head(10)

print(exemplos.to_string(index=False))



# ==================================================
# SPRINT 4 - INVESTIGACAO DOS DADOS
# ==================================================

print("\n=== SPRINT 4: INVESTIGACAO DOS DADOS ===", flush=True)

# Quantidade de compras, clientes e produtos distintos
print("\nCompras distintas (CO_ID):", df["CO_ID"].nunique())
print("Clientes distintos (CL_ID):", df["CL_ID"].nunique())
print("Produtos distintos (PR_ID):", df["PR_ID"].nunique())

# Quantidade de registros por cliente
print("\nTop 10 clientes por quantidade de registros:")
print(
    df["CL_ID"]
    .value_counts()
    .head(10)
    .to_string()
)

# Quantidade de registros por produto
print("\nTop 10 produtos por quantidade de registros:")
print(
    df["PR_NOME"]
    .value_counts()
    .head(10)
    .to_string()
)

# Quantidade de registros por categoria
print("\nQuantidade de registros por categoria:")
print(
    df["PR_CAT"]
    .value_counts()
    .to_string()
)

print("\nSprint 4 concluído.", flush=True)


# ==================================================
# SPRINT 5 - ESTATISTICA DESCRITIVA
# ==================================================

print("\n=== SPRINT 5: ESTATISTICA DESCRITIVA ===", flush=True)

coluna = df["CL_FHL"]

print("\nQuantidade de valores validos:", coluna.count())
print("Media:", coluna.mean())
print("Mediana:", coluna.median())
print("Desvio padrao:", coluna.std())
print("Moda:", coluna.mode().tolist())
print("Valor minimo:", coluna.min())
print("Valor maximo:", coluna.max())

print("\nQuartis:")
print(coluna.quantile([0.25, 0.50, 0.75]))

print("\nFrequencia por quantidade de filhos:")
print(coluna.value_counts().sort_index())

print("\nSprint 5 concluido.", flush=True)



# ==================================================
# SPRINT 6 - ANALISES POR AGRUPAMENTO
# ==================================================

print("\n=== SPRINT 6: AGRUPAMENTOS ===", flush=True)

# 1. Quantidade de registros por categoria
por_categoria = (
    df.groupby("PR_CAT")
    .size()
    .sort_values(ascending=False)
)

print("\n1. Registros por categoria:")
print(por_categoria.to_string())

# 2. Registros por genero
por_genero = (
    df.groupby("CL_GENERO")
    .agg(
        registros=("CL_ID", "size"),
        clientes_distintos=("CL_ID", "nunique"),
        media_filhos=("CL_FHL", "mean")
    )
    .sort_values("registros", ascending=False)
)

print("\n2. Analise por genero:")
print(por_genero.to_string())

# 3. Produtos com mais registros
por_produto = (
    df.groupby(["PR_ID", "PR_NOME"])
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("\n3. Top 10 produtos por registros:")
print(por_produto.to_string())

print("\nSprint 6 concluido.", flush=True)


print("\n=== SPRINT 7: VALIDACAO FINAL ===", flush=True)

# 1. Verificar se o cadastro dos clientes e consistente
cadastro_cliente = df.groupby("CL_ID").agg(
    generos_distintos=("CL_GENERO", "nunique"),
    estado_civil_distintos=("CL_EC", "nunique"),
    filhos_distintos=("CL_FHL", "nunique"),
    segmentos_distintos=("CL_SEG", "nunique")
)

print("\nClientes com mais de um valor de filhos:")
print((cadastro_cliente["filhos_distintos"] > 1).sum())

print("\nClientes com mais de um genero:")
print((cadastro_cliente["generos_distintos"] > 1).sum())

# 2. Comparar o impacto da remocao de duplicatas exatas
df_sem_duplicatas = df.drop_duplicates()

print("\nLinhas antes:", len(df))
print("Linhas apos remover duplicatas exatas:", len(df_sem_duplicatas))
print("Linhas removidas:", len(df) - len(df_sem_duplicatas))

# 3. Verificar categorias nao classificadas
print("\nRegistros com categoria #N/D:")
print((df["PR_CAT"].astype(str).str.strip() == "#N/D").sum())

print("\nSprint 7 concluido.", flush=True)


print("\n=== SPRINT 8: PERFIL DOS CLIENTES ===", flush=True)

# Uma linha por cliente, sem alterar a base principal
clientes = df[
    ["CL_ID", "CL_GENERO", "CL_EC", "CL_FHL", "CL_SEG"]
].drop_duplicates(subset="CL_ID")

print("Clientes unicos:", len(clientes))

print("\nEstatistica da quantidade de filhos por cliente:")
print(clientes["CL_FHL"].describe())

print("\nDistribuicao de filhos por cliente:")
print(
    clientes["CL_FHL"]
    .value_counts()
    .sort_index()
    .to_string()
)

print("\nPercentual de clientes por quantidade de filhos:")
print(
    (clientes["CL_FHL"].value_counts(normalize=True).sort_index() * 100)
    .round(2)
    .to_string()
)

print("\nClientes por genero:")
print(clientes["CL_GENERO"].value_counts().to_string())

print("\nSprint 8 concluido.", flush=True)




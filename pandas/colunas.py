import pandas as pd

df = pd.read_csv("data/transacoes.csv", sep=";")

print(df.shape) #linhas e colunas do df
print(df.dtypes)

# new_df=df.rename(columns={"qtdePontos":"qtPontos",
#                           "descSistemaOrigem":"SistemaOrigem"})
renamed_colums = {"QtdePontos":"qtPontos",
                     "DescSistemaOrigem":"SistemaOrigem"
}
df.rename(columns=renamed_colums, inplace=True) #renomeia no próprio data frame

print(df.columns.tolist())

print(df[["IdCliente"]])  #dataframe
print(df["IdCliente"]) #series

print(df[["IdCliente","qtPontos"]].head(5))  

#reordenando as colunas

colunas = list(df.columns)
colunas.sort()
df = df[colunas]
print(df)
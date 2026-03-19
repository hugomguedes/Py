import pandas as pd

df_transacoes = pd.read_csv("data/transacoes.csv", sep=";")

print(df_transacoes.head())

print(df_transacoes.groupby(by=["IdCliente"]).count())

print(df_transacoes.groupby(by=["IdCliente"])[["IdTransacao"]].count())  

summary = (df_transacoes.groupby(by=["IdCliente"], as_index= False).agg({"IdTransacao": ["count"],
                                                                            "QtdePontos": ["sum", "mean"]})
                                                                            )
print (summary)

summary.columns = ["IdCliente", "QtdeTransacao", "TotalPontos", "avgPontos"]

print(summary)
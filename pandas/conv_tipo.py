import pandas as pd
df = pd.read_csv("data/clientes.csv", sep=";")

print(df["qtdePontos"].astype(int)) #convertendo para int

# df["DtCriacao"] = df["DtCriacao"].replace({"0000-00-00 00:00:00.000": "2024-02-02 09:00:00.000"})  #substitui a data antiga pelo novo valor

replace = {"0000-00-00 00:00:00.000": "2024-02-02 09:00:00.000"}
df["DtCriacao"] = pd.to_datetime(df["DtCriacao"].replace(replace))

print(df["DtCriacao"])

print(df["DtCriacao"].dt.month)
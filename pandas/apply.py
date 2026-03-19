import pandas as pd

df = pd.read_csv("data/clientes.csv", sep=";")

def getLastId(x):
    return x.split("-")[-1]

df["novoId"]=df["idCliente"].apply(getLastId)

print(df.info())
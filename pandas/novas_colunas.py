import pandas as pd 
df = pd.read_csv("data/clientes.csv", sep=";")

newDf= df.sort_values(by="qtdePontos", ascending = False).head()

print(newDf)

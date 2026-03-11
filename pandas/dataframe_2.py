import pandas as pd

df_clientes = pd.read_csv("data/clientes.csv", sep=";")


print(df_clientes.head(n=10))
print(df_clientes.tail(10)) #final do dataset
print(df_clientes.sample(10)) #10 amostras aleatórias

print(df_clientes.shape) #linhas e colunas do dataframe
print(df_clientes.columns) #lista das colunas do df
print(df_clientes.info(memory_usage='deep', max_cols=2))

print(df_clientes.dtypes["DtCriacao"])


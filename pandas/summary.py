import pandas as pd

clientes = pd.read_csv("data/clientes.csv", sep=";")

print(clientes["flTwitch"].sum())
print(clientes["flTwitch"].mean())

redes_sociais = ["flEmail", "flTwitch", "flYouTube", "flBlueSky", "flInstagram"]

print(clientes[redes_sociais].sum()) #calcula a agregação da serie

num_columns = clientes.dtypes[clientes.dtypes != "object"].index.tolist()
print(num_columns) #lista com as colunas com tipo diferente de objec

print(clientes[num_columns].mean())
print(clientes[num_columns].describe())
arquivo = "data.csv"

with open (arquivo) as openFile:
    lines = openFile.readlines()

for linha in lines:
    print(linha)

dados = dict()
chaves = lines[0].strip("\n").split(";")  #variaveis/label

for c in chaves:
    dados[c] = []


for l in lines[1:0]:
    valores = l.strip("\n").split(",")
    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])
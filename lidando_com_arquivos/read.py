nomeArquivo = "historia.txt"
# openFile = open(nomeArquivo)

# print(openFile.read())

# openFile.close()

with open(nomeArquivo) as openFile:
    conteudo = openFile.read()

print(conteudo)

txt = "meu novo arquivo"
nomeArquivo = "historia_02.txt"
with open(nomeArquivo, mode="w") as openFile:
    conteudo = openFile.write(txt)
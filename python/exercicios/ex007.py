# dicionario
dados = {
    "nome":"joao",
    "filhos": True,
    "cargos": [{"nome":"ds jr","empresa":"boticario"},
               {"nome":"ds sr", "empresa": "carasc"}]
}

dados["estado_civil"] = "solteiro" #adicionando
# print(dados["nome"])
# print([dados][-1])
# print([dados["cargos"][-1]["empresa"]])
# print("chaves ", dados.keys())
# print("valores ", dados.values())

# for i in dados:
#     print(i,"->", dados[i])

for chave, valor in dados.items():
    print(chave,"->",valor)
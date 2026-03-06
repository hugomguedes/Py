soma = 0
while True:
    entrada = input("digite o valor ")
    if entrada == "":
        break
    soma += float(entrada)

print (f"soma é {soma}")
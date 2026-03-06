frases = {}

while True:
    frase = input("digite frases ")
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase]+= 1

for i, j in frases.items():
    print(i,"->",j)
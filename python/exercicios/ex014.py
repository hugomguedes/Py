def numerosPares (lista):
    pares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
    
    return pares

for i in range (10):
    numeros = []
    numeros = int(input("digite os valores"))

print (numerosPares(numeros))
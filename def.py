# def juros_compostos (aporte, taxa, juros):
#     return aporte * (1 + taxa) ** juros


# print(juros_compostos (1000,0.13,5))


def par_impar (num:int):
    if num % 2 ==0:
        print("par")
    else:
        print ("impar")

numero = int(input("digite o numero "))
par_impar(numero)
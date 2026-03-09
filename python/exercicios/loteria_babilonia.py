# Construa um programa que realiza o sorteio de um numero entre 1 e 15.
# O usuário terá 3 chances de acertar o valor.
# A cada tentativa você deve informar se o chute é maior ou menor que o número sorteado.
# Caso o usuário acerte, dê os parabéns
import random
def getInput():
     while True:
        try:
            numeroUsuario = int(input("entre com o numero \n"))
        
        except ValueError as err:
            print("valor invalido")
            continue

        if 1 <= numeroUsuario <= 15:
            return numeroUsuario

        print("valor deve ser entre 1 e 15")

numeroSorteio = random.randint(1,15)

for i in range (3):

    numeroUsuario = getInput()

    if numeroSorteio == numeroUsuario:
        print("parabéns vc ganhou")
        break
    elif numeroUsuario > numeroSorteio:
        print("numero alto demais \n")
        
    else:
            print("numero baixo demais \n")
else:
    print("suas tentativas acabaram")
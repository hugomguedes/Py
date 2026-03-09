fruta = input("entre com o nome da fruta ")

frutas = {
    "Pera": "R$ 1,25",
    "Goiaba": "R$ 3,25",
    "Abaxaxi": "R$ 4,25",
    "Jaca": "R$ 0,25",
    "Laranja": "R$ 1,25",
    "Banana": "R$ 5,25"
}
if fruta in frutas:
    print(frutas[fruta])
else:
    print("entre com um valor valido")
num1 = float(input("digite o primeiro numero"))
num2 = float(input("digite o segundo numero"))
operation = input("selecione a operação desejada: + , - , / , *")

def calcular (num1, num2, operation):
    match operation:
        case "+":
            return num1+num2
        case "-":
            return num1-num2
        case "/":
            if (num2==0):
                return "não é possivel dividir por 0"
            return num1/num2
        case "*":
            return num1*num2
        case _:
            return "Operação invalida"


resultado = calcular(num1,num2,operation)

print(resultado)
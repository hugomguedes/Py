A = 1
B = 5

A , B = B , A

a, *resto, b = 1,2, 3, 4, 4,5,6, 666, #os outros valores vão para a variavel *resto
print(a,b,resto)

def soma (a,b,c,d):
    return a+b+c+d

values = [1,2,3,4]

print(soma(*values))

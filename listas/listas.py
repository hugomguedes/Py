x = []

for i in range (1,101):
    x.append(i)



y = [i for i in range (1,101)] # mesma coisa de cima

def par (x):
    return x % 2 == 0


z = [par(i) for i in range (1,101)]
print (z)
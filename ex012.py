cont = 0
for i in range (1000,2001):
    if  i % 11 == 2:
        print(i)
        cont += 1
print(f"total encontrados {cont}")
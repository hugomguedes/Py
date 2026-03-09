palavra = input("digite a palavra \n").lower()
count = 0
for i in palavra:
    if i == "a":
        count += 1

# count = palavra.count("a")
print(f"quantidade é {count}")
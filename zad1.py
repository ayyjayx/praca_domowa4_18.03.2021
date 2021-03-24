import random
for x in range (15):
    x = random.randint(0, 30) * 2
    x = str(x)
    plik = open("liczby.txt", "a")
    plik.write(x)
    plik.write("\n")
    plik.close()
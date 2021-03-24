plik = open("tekst.txt", "w")
plik.write("To\n")
plik.write("jest\n")
plik.write("zadanie\n")
plik.write("nr\n")
plik.write("3\n")
with open("tekst.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")
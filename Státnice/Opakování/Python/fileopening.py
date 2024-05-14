f = open("file.txt", "rt")

f.close()

with open("file.txt", "rt") as file:
    print(file.read(7))
    print(file.seek(0))
    print(file.read(7))

with open("file.txt", "rt") as file:
    radek = file.readline()
    while radek:
        print(radek)
        radek = file.readline()

with open("file.txt", "a+") as file:
    file.write("\ntoto bylo zapsáno")

try:
    # práce se souborem
    f = open("file.txt", "w+")
    f.write("Programování\n")
    f.write("v Pythonu je zábava.")
except:
    # ošetření výjimek
    print("Chyba při práci se souborem.")
    # uzavření souboru při výjimce
finally:
    f.close()
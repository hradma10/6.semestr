PRESNOST = 0.00000001
# výpočet druhé odmocniny čísla x pomocí Newtonovy metody
# https://cs.wikipedia.org/wiki/Metoda_tečen
def odmocnina(x):
    odhad = x
    while True:
        novy_odhad = 0.5 * (odhad + x / odhad)
        if abs(novy_odhad - odhad) < PRESNOST:
            return novy_odhad
        odhad = novy_odhad

# výpočet n-té mocniny čísla x
def mocnina(x, n):
    return float(x**n)
# test funkcí

if __name__ == "__main__":
    print(odmocnina(2))  # vypíše: 1.414213562373095
    print(odmocnina(4))  # vypíše: 2.0
    print(mocnina(2, 2))  # vypíše: 4
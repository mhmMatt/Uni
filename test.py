def finde_primzahlen(bis):
    """Gibt alle Primzahlen kleiner oder gleich bis zurück."""
    primzahlen = []

    for zahl in range(2, bis + 1):
        ist_primzahl = True
        for teiler in range(2, int(zahl**0.5) + 1):
            if zahl % teiler == 0:
                ist_primzahl = False
                break
        if ist_primzahl:
            primzahlen.append(zahl)

    return primzahlen


grenze = int(input("Primzahlen finden bis: "))
print(finde_primzahlen(grenze))

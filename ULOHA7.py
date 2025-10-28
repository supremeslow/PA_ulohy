

najmensie = None
najvacsie = None

print("Zadaj čísla jedno po druhom. Napíš 'koniec' pre ukončenie.")

while True:
    vstup = input("Zadaj číslo: ")
    if vstup.lower() == "koniec":
        break

    cislo = float(vstup)  

    if najmensie is None or cislo < najmensie:
        najmensie = cislo
    if najvacsie is None or cislo > najvacsie:
        najvacsie = cislo

if najmensie is not None:
    print(f"Najmenšie číslo: {najmensie}")
    print(f"Najväčšie číslo: {najvacsie}")
else:
    print("Nezadali ste žiadne číslo.")

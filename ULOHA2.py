# Program: Najväčšie z troch čísel (opakujúci sa)

while True:
    print("\nZadaj tri celé čísla (alebo napíš 'koniec' pre ukončenie):")

    # Možnosť ukončenia programu
    vstup = input("Zadaj prvé číslo alebo 'koniec': ")
    if vstup.lower() == "koniec":
        print("Program sa ukončuje. Dovidenia!")
        break

    # Pokus o konverziu prvého čísla
    try:
        a = int(vstup)
        b = int(input("Zadaj druhé číslo: "))
        c = int(input("Zadaj tretie číslo: "))
    except ValueError:
        print("Prosím, zadávaj len celé čísla!")
        continue

    # Určenie najväčšieho čísla (bez použitia max)
    if a >= b and a >= c:
        najvacsie = a
    elif b >= a and b >= c:
        najvacsie = b
    else:
        najvacsie = c

    print("Najväčšie číslo je:", najvacsie)

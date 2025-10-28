# Program: Počet párnych a nepárnych čísel (opakujúci sa, bez kontroly vstupu)

while True:
    vstup = input("\nZadaj počet čísel alebo 'koniec' pre ukončenie: ")
    if vstup.lower() == 'koniec':
        print("Program sa ukončuje. Dovidenia!")
        break

    pocet = int(vstup)

    parne = 0
    neparne = 0

    for i in range(pocet):
        cislo = int(input(f"Zadaj číslo {i+1}: "))
        if cislo % 2 == 0:
            parne += 1
        else:
            neparne += 1

    print(f"Počet párnych čísel: {parne}")
    print(f"Počet nepárnych čísel: {neparne}")

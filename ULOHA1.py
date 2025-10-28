
while True:
    # nacitanie vstupov
    cislo1 = float(input("Zadaj prvé číslo: "))
    operacia = input("Zadaj operáciu (+, -, *, / alebo 'koniec' na ukončenie): ")

    # koniec programu
    if operacia.lower() == 'koniec':
        print("Program sa ukončuje. Dovidenia!")
        break

    cislo2 = float(input("Zadaj druhé číslo: "))

    # vypocty
    if operacia == '+':
        vysledok = cislo1 + cislo2
        print("Výsledok:", vysledok)
    elif operacia == '-':
        vysledok = cislo1 - cislo2
        print("Výsledok:", vysledok)
    elif operacia == '*':
        vysledok = cislo1 * cislo2
        print("Výsledok:", vysledok)
    elif operacia == '/':
        if cislo2 != 0:
            vysledok = cislo1 / cislo2
            print("Výsledok:", vysledok)
        else:
            print("Chyba: delenie nulou nie je povolené.")
    else:
        print("Zle zadaný znak.")

    print()  

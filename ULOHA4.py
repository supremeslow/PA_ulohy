# Program: Jednoduchý bankomat

spravny_pin = "1234"  # nastavený PIN
pokusy = 3
zostatok = 0.0

# Overenie PINu
while pokusy > 0:
    pin = input("Zadaj svoj PIN: ")
    if pin == spravny_pin:
        print("PIN správny. Vitaj v bankomate!")
        break
    else:
        pokusy -= 1
        print(f"PIN nesprávny. Zostáva pokusov: {pokusy}")
else:
    print("Vyčerpané pokusy. Prístup zamietnutý.")
    exit()  # ukončí program

# Menu bankomatu
while True:
    print("\nMenu:")
    print("1 - Zostatok")
    print("2 - Vklad")
    print("3 - Výber")
    print("4 - Koniec")

    volba = input("Zadaj číslo operácie: ")

    if volba == "1":
        print(f"Tvoj zostatok je: {zostatok} €")
    elif volba == "2":
        castka = float(input("Zadaj sumu na vloženie: "))
        zostatok += castka
        print(f"Vklad úspešný. Nový zostatok: {zostatok} €")
    elif volba == "3":
        castka = float(input("Zadaj sumu na výber: "))
        if castka > zostatok:
            print("Chyba: Nedostatok peňazí na účte!")
        else:
            zostatok -= castka
            print(f"Výber úspešný. Nový zostatok: {zostatok} €")
    elif volba == "4":
        print("Dovidenia!")
        break
    else:
        print("Neplatná voľba. Skús znova.")

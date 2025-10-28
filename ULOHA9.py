# Program: Analýza čísel v rozsahu a, b

# Načítanie vstupov
a = int(input("Zadaj prvé číslo (a): "))
b = int(input("Zadaj druhé číslo (b): "))

# Uisti sa, že a <= b
if a > b:
    a, b = b, a

parne = []
neparne = []
delitelne_3 = []

for cislo in range(a, b + 1):
    if cislo % 2 == 0:
        parne.append(cislo)
    else:
        neparne.append(cislo)
    if cislo % 3 == 0:
        delitelne_3.append(cislo)

print(f"Párnych čísel: {len(parne)} -> {parne}")
print(f"Nepárnych čísel: {len(neparne)} -> {neparne}")
print(f"Deliteľných tromi: {len(delitelne_3)} -> {delitelne_3}")

# Program: Počet slov a dĺžka najdlhšieho slova

veta = input("Zadaj vetu: ")

# Rozdelenie vety na slová podľa medzier
slova = veta.split()

# Počet slov
pocet_slov = len(slova)

# Dĺžka najdlhšieho slova
if slova:
    najdlhsie_slovo = max(slova, key=len)
    dlzka_najdlhsieho = len(najdlhsie_slovo)
else:
    dlzka_najdlhsieho = 0

print(f"Počet slov: {pocet_slov}")
print(f"Dĺžka najdlhšieho slova: {dlzka_najdlhsieho}")

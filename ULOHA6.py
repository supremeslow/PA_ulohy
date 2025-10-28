import random

pocet_hodov = 0

print("Hádžem kockou, až kým nepadne 6...")

while True:
    hod = random.randint(1, 6)
    pocet_hodov += 1
    print(f"Hod {pocet_hodov}: padlo {hod}")
    if hod == 6:
        print(f"Šestka padla po {pocet_hodov} hodoch!")
        break

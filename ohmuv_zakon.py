# Výpočet podle Ohmova zákona

U = float(input("Zadej napětí [V]: ")) # Napětí [V]
R = float(input("Zadej odpor [Ohm]: ")) # Odpor [Ohm] 
t = float(input("Zadej dobu průchodu proudu [s]: ")) # Odpor [Ohm] 

# Výpočet proudu
I = U / R

# Výpočet výkonu
P = U * I

# Energie
W = P * t

print("Elektrotechnická kalkulačka")
print("----------------------------")
print(f"Napětí: {U} V")
print(f"Odpor: {R} Ohm")
print(f"Proud: {I} A")
print(f"Výkon: {P} W")
print(f"Energie za {t} sekund: {W} J")

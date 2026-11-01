# Výpočet podle Ohmova zákona

U = input()       # Napětí [V]
R = input()      # Odpor [Ohm]

# Výpočet proudu
I = U / R

# Výpočet výkonu
P = U * I

print("Elektrotechnická kalkulačka")
print("----------------------------")
print(f"Napětí: {U} V")
print(f"Odpor: {R} Ohm")
print(f"Proud: {I} A")
print(f"Výkon: {P} W")

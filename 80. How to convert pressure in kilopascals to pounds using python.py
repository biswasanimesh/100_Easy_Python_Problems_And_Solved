kpa = float(input("Enter pressure in Kilopascals : "))

psi = kpa / 6.89475

mmhg = kpa * 760 / 101.325
atm = kpa / 101.325

print(psi)
print(mmhg)
print(atm)
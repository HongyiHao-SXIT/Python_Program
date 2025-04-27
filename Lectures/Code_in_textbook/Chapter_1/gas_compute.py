gallons = float(input("Please enter the number of gallons of gasoline (as a floating-point number): "))

gallon_to_litre = 3.785412

barrel_to_gallon = 19.5

carbon_dioxide_per_gallon = 20

gas_energy = 115000

ethanol_energy = 75700

unit_price = 3.00

litres = gallons * gallon_to_litre

barrels = gallons / barrel_to_gallon

carbon_dioxide = gallons * carbon_dioxide_per_gallon

ethanol_gallons = (gallons * gas_energy) / ethanol_energy

cost = gallons * unit_price

print(f"Quantity in litres: {litres} litres")

print(f"Number of barrels of oil needed to produce this gasoline: {barrels} barrels")

print(f"Amount of carbon dioxide produced (in pounds): {carbon_dioxide} pounds")

print(f"Equivalent number of gallons of ethanol in terms of energy: {ethanol_gallons} gallons")

print(f"Price (in dollars): {cost} dollars")
converters = [
    lambda t: t * 1000,
    lambda kg: kg * 1000,
    lambda g: g * 1000,
    lambda mg: mg * 0.00000220462262
]

tonns = float(input("Enter weight in tonns: "))

kg = converters[0](tonns)
g = converters[1](kg)
mg = converters[2](g)
lbs = converters[3](mg)

print(kg, "kg")
print(g, "gm")
print(mg, "mg")
print(lbs, "lbs")
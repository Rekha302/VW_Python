num = int(input("Enter a 4 digit number: "))

d1 = num // 1000
d2 = (num % 1000) // 100
d3 = (num % 100) // 10
d4 = num % 10

print("a.", d1, d2, d3, d4)

print("b.", num, "=", d1*1000, "+", d2*100, "+", d3*10, "+", d4)

reverse = d4*1000 + d3*100 + d2*10 + d1
print("c.", reverse)

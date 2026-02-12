t = tuple(input("Enter tuple elements separated by space: ").split())
value = input("Enter value to find: ")

count = t.count(value)

if count > 1:
    print("Repeated", count, "times")
else:
    print("Not repeated")


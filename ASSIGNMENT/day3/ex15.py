num = [2,3,4,5,2,6,3,2]
result = []

for i in num:
    if i not in result:
        result.append(i)

print("Result:", result)
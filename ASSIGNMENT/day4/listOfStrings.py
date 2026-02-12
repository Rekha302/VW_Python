list1 = [1,2,3,4]
tuple1 = (5,6,7,8)

result = list(map(str, list1)) + list(map(str, tuple1))
print(result)

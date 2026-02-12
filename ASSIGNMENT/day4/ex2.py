def union(list1, list2):
    result = list1.copy()
    for x in list2:
        if x not in result:
            result.append(x)
    return result

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

print(union(list1, list2))
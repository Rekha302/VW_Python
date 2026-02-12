def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False
l1 = input("Enter first list elements: ").split()
l2 = input("Enter second list elements: ").split()

print(overlapping(l1, l2))
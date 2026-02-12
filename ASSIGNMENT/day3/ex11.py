
lst = [10, 20, 30, (40, 50), 60]

count = 0
for item in lst:
    if isinstance(item, tuple):
        break
    count += 1

print(count)






def display_list(lst):
    for item in lst:
        if item.isdigit():
            print(item * 3)
        else:
            print(item + "#")

mylist = ['41','DROND','BVSs','13','ZARA']
display_list(mylist)



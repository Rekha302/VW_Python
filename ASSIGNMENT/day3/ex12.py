def display_list(lst):
    for item in lst:
        if item.isdigit():
            print(item * 3)
        else:
            print(item + "#")

mylist = ['41','DROND','BVSs','13','ZARA']
display_list(mylist)



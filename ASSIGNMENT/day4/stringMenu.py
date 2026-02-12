def even_pos(s):
    print(s[1::2])

def odd_pos(s):
    print(s[0::2])

def length(s):
    print(len(s))

def add_a(s):
    print(s + "a"*len(s))

s = input("Enter string: ")

choice = input("A/B/C/D: ")

if choice == "A":
    even_pos(s)
elif choice == "B":
    odd_pos(s)
elif choice == "C":
    length(s)
elif choice == "D":
    add_a(s)


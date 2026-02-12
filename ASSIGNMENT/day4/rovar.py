def translate(text):
    vowels = "aeiouAEIOU "
    result = ""
    for char in text:
        if char not in vowels and char.isalpha():
            result += char + "o" + char
        else:
            result += char
    return result

text = input("Enter text: ")
print(translate(text))


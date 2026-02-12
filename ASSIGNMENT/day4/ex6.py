text = """Python is a high-level, general-purpose programming language. Its design philosophy emphasizes code readability with the use of significant indentation. Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including structured, object-oriented and functional programming."""

text = text.lower()
count = {}

for char in text:
    if char.isalpha():
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

print(count)
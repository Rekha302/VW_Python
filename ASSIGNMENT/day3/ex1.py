for num in range(0, 11):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print("Factorial of", num, "=", factorial)
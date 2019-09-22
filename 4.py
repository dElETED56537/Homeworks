palindrome = 1

for i in range(100, 1000):
    for j in range(100, 1000):
        multiplication = i * j
        if str(multiplication) == str(multiplication)[::-1]:
            if multiplication > palindrome:
                palindrome = multiplication
print(palindrome)



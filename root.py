n = float(input("number = "))
x = n
for i in range(5):
    x = 0.5 * (x + n / x)
print("Square root =", x)

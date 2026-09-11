import math

while True:
    try:
        x = float(input("Enter a positive real number x: "))
        if x > 0:
            break
        else:
            print("x must be a positive number")
    except ValueError:
        print("Please enter a valid real number")

while True:
    try:
        y = int(input("Enter a positive integer y: "))
        if y > 0:
            break
        else:
            print("y must be a positive integer")
    except ValueError:
        print("Please enter a valid integer")
z = x ** y
log2x = math.log2(x)
log2y = math.log2(y)

print("\nResults:")
print("x =", x)
print("y =", y)
print("x raised to the power of y =", z)
print("log2(x) =", round(log2x, 4))
print("log2(y) =", round(log2y, 4))
import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
D = b ** 2 - 4 * a * c
x1 = (-b + math.sqrt(D)) / 2 * a
x2 = (-b - math.sqrt(D)) / 2 * a
print(f"x1 = {x1}; x2 = {x2}")

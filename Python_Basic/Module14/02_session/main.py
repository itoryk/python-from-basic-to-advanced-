print("Введите первую точку")
x1 = float(input('X: '))
y1 = float(input('Y: '))
print("\nВведите вторую точку")
x2 = float(input('X: '))
y2 = float(input('Y: '))
k = 0
b = 0
x_diff = x1 - x2
y_diff = y1 - y2
if x_diff != 0:
    k = y_diff / x_diff
    b = y2 - k * x2

print("Уравнение прямой, проходящей через эти точки:")
print("y = ", k, " * x + ", b)

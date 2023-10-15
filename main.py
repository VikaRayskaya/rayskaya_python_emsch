a = int(input())
b = int(input())
c = int(input())

e = a + b + c
d = e / 3
print("среднее", d)

g = 1 / a + 1 / b + 1 / c
f = 3 / g
print("гармоническое", f)

data = sorted([ a, b, c])
print("медиана", data[1])

data = sorted([ a, b, c])
y = data[2] ** data[0] / d
print("абадакадабра", y)
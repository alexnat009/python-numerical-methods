a = 4.9 - 4.845
b = a == 0.055
print(a)
print(b)

print(1 - 1 / 3 + 1 / 3)


def add_and_subtract(iter):
    res = 1
    for i in range(iter):
        res += 1 / 3
    for i in range(iter):
        res -= 1 / 3
    return res


print(add_and_subtract(100))
print(add_and_subtract(1000))
print(add_and_subtract(10000))

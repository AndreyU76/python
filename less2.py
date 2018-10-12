a = [3, 5.1, 7, 4, 6, 8, 9]
b = []

for x in a:
    if x % 2 == 0:
        b.append(x / 4)
    else:
        b.append(x*2)

print(b)

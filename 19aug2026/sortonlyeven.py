nums = [5, 2, 8, 1, 6, 3, 4]

even_nos = []

for x in nums:
    if x % 2 == 0:
        even_nos.append(x)

for i in range(len(even_nos)):
    for j in range(len(even_nos) - 1 - i):
        if even_nos[j] > even_nos[j + 1]:
            even_nos[j], even_nos[j + 1] = even_nos[j + 1], even_nos[j]

print(even_nos)
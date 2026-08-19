vlist = [100, 5, 23, 7, 1000]

for i in range(len(vlist)):
    for j in range(len(vlist) - 1 - i):
        if len(str(vlist[j])) > len(str(vlist[j + 1])):
            vlist[j], vlist[j + 1] = vlist[j + 1], vlist[j]

print(vlist)
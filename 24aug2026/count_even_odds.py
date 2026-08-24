odd = 0
even = 0
arr=[1,5,3,5,3,8,90,3]
for x in arr:
    if x % 2 == 0:
        even += 1
    else:
     odd += 1

print(odd, even) 
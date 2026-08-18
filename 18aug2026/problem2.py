# import numpy as np

a=[3,4,2,54,2,2]

#d=np.array(a)

# sum=0
# for i in a:
#     sum = sum + i
    
# # print(sum)
# print(sum/len(a))
d= sum(a)

# print(d)

# for i in range(len(a)-1):
#     if a[i]==a[i+1]:
#         print(f"the number {a[i]} is repeated: true")
#     else:
#         print("false")

#     i=i+1

# a=[3,4,2,54,2,2]
# set1 = set(a)

# print(set1)

# for i in min(len(set1) and len(a)):
#     if set[i]==a[i]



# duplicate = False

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             duplicate = True
            

# print(duplicate)    



a = [3, 4,3,3, 2, 54, 2, 2]

set1 = set(a)

for x in set1:
    if a.count(x) > 1:
        print(x)





items=[1,2,3,4,4,5,5,5,6,9,9] 

dup=[]

for i in items:
    if items.count(i)>1:
        if i not in dup:
            dup.append(i)

print(dup) 




# dup = []

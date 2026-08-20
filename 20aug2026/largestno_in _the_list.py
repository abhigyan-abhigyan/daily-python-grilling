# arr=[1, 8, 7, 56, 90]

# vlist=[]
# if len(arr)==1:
#     print(vlist[0])
# for i in range(len(arr)):
#  if arr[i]>arr[i+1]:
#     vlist.append(arr[i])
#     i=i+1
# else:
#  vlist.append(arr[i+1])



arr=[1, 8, 7, 56, 90]

a=sorted(arr)

print(a[len(a)-1])
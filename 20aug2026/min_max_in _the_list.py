#MIN AND MAX NUMBER IN THE LIST
arr=[1, 4, 3, 5, 8, 6]
for i in range(len(arr)):
            for j in range(len(arr) - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        
vlist=[]
        
vlist.append(arr[0])
print(vlist)
vlist.append(arr[len(arr)-1])
print(vlist)
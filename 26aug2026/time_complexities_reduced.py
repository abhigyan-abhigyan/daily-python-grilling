
arr = [2, 3, 1, 2, 3]
def leaders(arr):
    # code here\
    vlist=[]
    max_element=0
    max_element=arr[-1]
    vlist.append(max_element)
    for j in range (len(arr)-2,-1,-1):
        if arr[j]>=max_element:
            max_element=arr[j]
            vlist.append(max_element)
    vlist.sort(reverse=True)
    return vlist

print(leaders(arr))

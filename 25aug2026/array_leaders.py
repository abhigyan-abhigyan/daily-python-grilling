
arr = [16, 17, 4, 3, 5, 2]

def leaders( arr):
    array_leaders=list()
    for i in range(len(arr)):
        if i==(len(arr)-1): 
            array_leaders.append(arr[i])
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                if j==(len(arr)-1): 
                    array_leaders.append(arr[i])
                
            else:
                break
            
                
                
            # else:
            #     i+=1     
            #     break

    return array_leaders       

print(leaders(arr))
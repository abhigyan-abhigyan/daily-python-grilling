
def intersection(num_1,num_2):
    least= set(num_1) if len(num_1)<len(num_2) else num_2
    greater= num_1 if len(num_1)>len(num_2) else num_2

   
    for num in least:
        common=set()
        if num in greater:
            common.add(num)
    return list(common)

num_1=[1,3,2,4,5]
num_2=[1,3,9,1]
print(intersection(num_1,num_2))




#whether the array is pallindrome or not

# arr = [1, 2, 3, 2, 1]

# #d=str(arr)
# length=len(arr)

# if length%2==0:
#     a=arr[:int(length/2-2)]
#     b=arr[(length+1):]
#     b.reverse()
#     if b==a:
#         print(True)
#     else:
#         print(False)
# else:
#     c=arr[:int((length-1)/2)-1] 
#     d=arr[int((length-1)/2)+1:]
#     d.reverse()==c
#     if d==c:
#         print(True)
#     else:
#         print(False)    

                  
    
#2nd attempt

arr = [1, 2, 3, 1]
b=arr[::-1] 

if arr==b:
    print(True)
else:
    print(False)

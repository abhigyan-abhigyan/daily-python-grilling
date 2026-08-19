
count=0
prime_list=list()    
start_no = int(input("enter the range of numbers, starting no: "))
end_no = int(input("ending no:"))

if start_no==0 or start_no==1:
   start_no=2
   
for i in range(start_no, end_no+1):
    divisible=False
    for j in range(2, i):
       if i%j==0:
        divisible=True
        break
    if divisible:
      count=count+1
      prime_list.append(i)

print(prime_list)          
print(count)          

count=0
prime_list=list()    
start_no = int(input("enter the range of numbers, starting no: "))
end_no = int(input("ending no:"))

if start_no==0 or start_no==1:
   start_no=2

for i in range(start_no, end_no+1):
    is_divisible = False
    for j in range(2, start_no):
        if i % j == 0:
            is_divisible = True
            break
    if not is_divisible:
        prime_list.append(i)
        count += 1

 








        # if i==j:
        #  count=count+1
        #  prime_list.append(i)
        #  i=i+1
        #  print("count up untilnow is :", i)
         
        # elif i%j!=0:
           
        #    j=j+1
        # else:
        #    j=j+1

           
   
        

for i in range(len(prime_list)):
    for j in range(len(prime_list) - 1 ):
        if(prime_list[j]) >(prime_list[j + 1]):
         (prime_list[j]),(prime_list[j + 1]) =(prime_list[j + 1]),(prime_list[j])

print("ascending prime list:")
print(prime_list)

for i in range(len(prime_list)):
    for j in range(len(prime_list) - 1 ):
        if prime_list[j] < prime_list[j + 1]:
            prime_list[j], prime_list[j + 1] = prime_list[j + 1], prime_list[j]
print("descending prime list:")
print(prime_list)

print(count)

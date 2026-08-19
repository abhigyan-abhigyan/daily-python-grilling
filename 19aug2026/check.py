count=0
prime_list=list()    
start_no = int(input("enter the range of numbers, starting no: "))
end_no = int(input("ending no:"))

if start_no==0 or start_no==1:
   start_no=2

for i in range(start_no, end_no+1):
    is_divisible = False
    for j in range(2, i):
        if i % j == 0:
            is_divisible = True
            break
    if not is_divisible:
        prime_list.append(i)
        count += 1

print(prime_list)

print(f"no of prime numbers in the list are:",count)
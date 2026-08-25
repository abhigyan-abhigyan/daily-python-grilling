arr=[2,3,1,2,3]

c=set(arr)
a=len(arr)
d=len(c)

orig_sum=arr.sum()

set_sum=d.sum()


numbers = [10, 20, 30, 20, 40, 20]
target = 10

while target in numbers:
    numbers.remove(target)

while target in numbers:
    numbers.remove(numbers)
    print('the most recurring element is: ', target)


print(numbers)



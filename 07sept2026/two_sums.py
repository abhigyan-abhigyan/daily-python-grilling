def two_sum(numbers, target):
    seen={}
    for i, numbers in enumerate(numbers):
        complement= target - numbers
        if complement in seen:
            return [seen[complement],i]

    return []

numbers=[1,3,2,4,5]
target= int(input("enter target number:"))
print("indices of the two numbers are:", two_sum(numbers, target))





        
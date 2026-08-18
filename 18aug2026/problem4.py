#bubble-sort

nums = [5, 2, 8, 1, 3]

nums = [5, 2, 8, 1, 3]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)


#descending order


for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)

#sorting only even numbers

nums = [5, 2, 8, 1, 6, 3, 4]

evens = []

for x in nums:
    if x % 2 == 0:
        evens.append(x)

for i in range(len(evens)):
    for j in range(len(evens) - 1 - i):
        if evens[j] > evens[j + 1]:
            evens[j], evens[j + 1] = evens[j + 1], evens[j]        

index = 0

for i in range(len(nums)):
    if nums[i] % 2 == 0:
        nums[i] = evens[index]
        index += 1

print(nums)            



#finding 3rdsmallest number in the list


nums = [7, 2, 9, 4, 1, 5]

for i in range(len(nums)):
    for j in range(len(nums) - 1 - i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

print(nums)
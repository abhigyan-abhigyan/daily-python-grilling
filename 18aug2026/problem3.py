nums=[23,67,12,89,45]

collections = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i]>nums[j] and nums[i]>=collections[0]:
            collections[0]=nums[i]
        else:
            collections[0]=nums[j]
print(collections[0])

                
ßßß
#finding missing element in a list containing numbers ranging from 0-n with list size of n-1(GFG)


# class Solution:
#     def missingNum(self, arr):

#         count = list()

#         b = sorted(arr)
#         if b[0] != 1:
#            count.append(1)

#         for i in range(1, len(b)):
#             if b[i] == b[i - 1] + 1:
#                i = i + 1
#             else:
#                 count.append(b[i - 1] + 1)

#         return count[0]
# n=2
# arr=[4,5,3,3]
# t=list()
# arr.append(n+1)
# print(type(t))

# total_sum=''
# count=total_sum

arr=[3,4,5,1]

a=sum(arr)
n=len(arr)+1
print(n)
t=n*(n+1)/2

        # list_sum=b*(b+1)/2
        # list_sum1=a*(a+1)/2
count=int(t-a)
        
print(count)  
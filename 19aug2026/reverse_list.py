#string reversal()

a="this is good"

b=a[::-1]
print(b)

c=a[:3:-1]
print(c)

#sorting a list

vlist=[2,3,4,2,66,55,22]

for i in range(len(vlist)):
    for j in range(len(vlist)-1-i):
        if (vlist[j])>(vlist[j+1]):
            (vlist[j], vlist[j+1])=(vlist[j+1], vlist[j])
  





print(vlist)







#list reversal
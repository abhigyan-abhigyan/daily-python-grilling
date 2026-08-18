user=input("enter the number up to which you wannaprint fizz and buzz to: ")

list1= list(range(1,int(user)+1))

print(list1)

for i in list1:
    if (i%3==0 and i%5==0):
     print("fizzbuzz")
    elif i%3==0:
       print("fizz")
    elif i%5==0:
        print("buzz")

    else:
        print(i)
    
    
timex=list(range(1,int(user)))
#Take an integer n and print an n × n grid showing the row and column positions.



n=int(input("enter the number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"({i},{j})", end=" ")
        if j==n:
            print("\n")
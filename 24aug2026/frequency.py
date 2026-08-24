count_x = 0
count_y = 0

for num in arr:
    if num == x:
        count_x += 1

    if num == y:
        count_y += 1
    if count_x > count_y:
       print(x)
    elif count_y > count_x:
       print(y)
    else:
        print(min(x, y))
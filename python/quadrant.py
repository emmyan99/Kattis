x = int(input())
y = int(input())

if x > 0:
    if y > 0:
        print(1) #x,y pos
    else:
        print(4) #x pos, y neg
else:
    if y < 0:
        print(3) #x,y neg
    else:
        print(2) #x neg, y pos
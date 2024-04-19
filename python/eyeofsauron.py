x = input()

partitioned = x.partition("()")
countLeft = 0
countRight = 0

for left in partitioned[0]:
    countLeft+=1
    
for right in partitioned[2]:
    countRight+=1

if countRight == countLeft:
    print("correct")
else:
    print("fix")

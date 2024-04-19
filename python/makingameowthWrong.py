# N - meowth will read every Nth page
# P - the amount of pages we read
# X - time for me to read 1 page
# Y - time for meowth to read 1 page

n, p, x, y = input().split()
n, p, x, y = [int(n), int(p), int(x), int(y)]
readingTime = 0

for i in range(p):
    print("readingTime: ", str(readingTime))
    if i == 0:
        readingTime += x
        continue
    elif(i % (n-1) == 0): 
        readingTime += y
        n += n
        continue
    else:
        readingTime += x
        continue


print(readingTime)


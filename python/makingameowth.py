# N - meowth will read every Nth page
# P - the amount of pages I read
# X - time for me to read 1 page
# Y - time for meowth to read 1 page

n, p, x, y = input().split()
n, p, x, y = [int(n), int(p), int(x), int(y)]
readingTime = 0

for i in range(p):
    readingTime += x

for j in range((n-1), p, (n-1)):
    readingTime += y

if (p % (n-1) == 0):
    readingTime += y


print(readingTime)



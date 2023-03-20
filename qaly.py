x = int(input())

res = 0

for i in range(x):
    y, z = input().split()
    y, z = [float(y), float(z)]
    res += (y*z)
    
print(res)
    
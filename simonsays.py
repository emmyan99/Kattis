x = int(input())

res = ""

for i in range(x):
    said = input()
    if (said[0:10] == "Simon says"):
        res += said[11:len(said)] + "\n"

print(res)





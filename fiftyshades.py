x = int(input())

result = []
count = 0

for i in range(x):
    y = input()
    txt = y.casefold()
    if txt.find("rose") >= 0 or txt.find("pink") >= 0:
        result.append(True)
        count += 1

if True in result:
    print(count)
else:
    print("I must watch Star Wars with my daughter")


    

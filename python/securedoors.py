x = int(input())

building = []
output = []

for i in range(x):
    line = input()

    if(line.find("entry") > -1):
        name = line[6:]
        if name in building:
            output.append(name + " entered (ANOMALY)")
        else:
            output.append(name + " entered")
            building.append(name)

    if(line.find("exit") > -1):
        name = line[5:]
        if name in building:
            output.append(name + " exited")
            building.remove(name)
        else:
            output.append(name + " exited (ANOMALY)")
        
for i in output: 
    print(i) 
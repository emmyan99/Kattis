import re

def main():
    lines = []
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:
            break

    #print(lines)
    loglines = []
    for line in lines:
        if line == "OPEN":
            daylines = []
            continue
        if line == "CLOSE":
            loglines.append(daylines)
            continue
        daylines.append(line)

    for logline in loglines:
        print(logline)




            #while line != "CLOSE":
             #   print(line)
             #   daylines.append(line)

            

#def open():
    #while(True):
        #msg = input()
    #entered = set()
    #exited = {}
    #exited = {
    #       "name" :{
    #   "entrymin" : 5,
    #   "exitmin"  : 35
    #},
    #name_pattern = r'^(EXIT|ENTER)\s+(\w+)\s+\d{1,3}$'

    #if msg == "CLOSE":
       #return
    #else:
        #if msg.find("ENTER") != -1:
            #name = re.match(name_pattern, msg).group(2)
            #entrymin = int((msg.partition(name))[2])
            #newEntry = {'entrymin':entrymin, 'exitmin':0}
            #exited[name] = newEntry 
            #for x in exited.values():
            #    print(x)
        #elif msg.find("EXIT") != -1:
            #name = re.match(name_pattern, msg).group(2)
            #exitmin = int((msg.partition(name))[2])
            #exited[name][exitmin] = exitmin
            #for x in exited.values():
                #print(x)

main()

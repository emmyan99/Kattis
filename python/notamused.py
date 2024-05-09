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
    
    # print(daylines)
    days = []
    name_pattern = r'^(EXIT|ENTER)\s+(\w+)\s+\d{1,3}$'
    for day in loglines:
        details = []
        for entry in day:
            if entry.find("ENTER") != -1:
                name = re.match(name_pattern, entry).group(2)
                entrymin = int((entry.partition(name))[2])
                if find_in_dict(name, details):
                    for dict in details:
                        if dict["name"] == name:
                            dict["entrymin"] == entrymin
                else:
                    newentry = {"name": name, "entrymin": entrymin, "price": 0} #price will be calc later, entrymin until EXIT
                    print(newentry)
                    details.append(newentry)

            elif entry.find("EXIT") != -1:
                name = re.match(name_pattern, entry).group(2)
                exitmin = int((entry.partition(name))[2])
                for dict in details:
                    if dict["name"] == name:
                        # print(dict["name"])
                        dict["price"] == dict["price"] + ((exitmin - dict["entrymin"])*0.1)
                        # print(dict["price"] + (exitmin-dict["entrymin"])*0.1)
                        #last price is wrong
                        dict["entrymin"] == 0
        days.append(details)



def find_in_dict(val, list_of_dicts):
    for dict in list_of_dicts:
        if val in dict.values():
            return True
    return False






#(exitmin - entrymin) * 0.1









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

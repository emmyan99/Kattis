import re

def main():
    inputlogs = input()
    daycounter = 0

    inputlogs = inputlogs.splitlines()
    print(inputlogs)
   # if inputlogs[0] == "OPEN":
    #    print(inputlogs)

    #input is a number of lines of text, unknown how many, need to figure out how to handle this kind of input

        

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

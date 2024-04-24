import re

def main():
    start = input()

    if start == "OPEN":
        open()
    print("yaay")

def open():
    msg = input()
    #entered = set()
    exited = {{}}
    #exited = {
    #       "name" :{
    #   "entrymin" : 5,
    #   "exitmin"  : 35
    #},
    name_pattern = r'^(EXIT|ENTER)\s+(\w+)\s+\d{1,3}$'

    if msg == "CLOSE":
       return
    else:
        if msg.find("ENTER") != -1:
            #entered.add(re.match(name_pattern, msg).group(2))

        elif msg.find("EXIT") != -1:



main()

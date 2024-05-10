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
                    for detail in details:
                        if detail["name"] == name:
                            detail["entrymin"] = entrymin
                else:
                    newentry = {"name": name, "entrymin": entrymin, "price": 0} #price will be calc later, entrymin until EXIT
                    details.append(newentry)

            elif entry.find("EXIT") != -1:
                name = re.match(name_pattern, entry).group(2)
                exitmin = int((entry.partition(name))[2])
                for detail in details:
                    if detail["name"] == name:
                        detail["price"] = detail["price"] + ((exitmin - detail["entrymin"])*0.1)

                        detail["entrymin"] = 0

        details = sorted(details, key=lambda x: list(x.values())[0])
        print(details)
        days.append(details)
        
    printLog(days)

def find_in_dict(val, list_of_dicts):
    for dict in list_of_dicts:
        if val in dict.values():
            return True
    return False


def printLog(dayslog):
    dayCounter = 1
    for day in dayslog:
        print("Day ", dayCounter)
        dayCounter += 1

        for entry in day:
            # print(entry["name"], " $",(f'{entry["price"]:.2f}'))
            print('{} ${}'.format(entry["name"],(f'{entry["price"]:.2f}')))


main()

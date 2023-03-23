x=1
resultList = []               #create list of lists of result dicts

while(x != 0):
    dict = {}
    x = int(input()) #no. of customers
    
    for i in range(x): 
        line = input()
        line = line.split() # "Alice bacon eggs spam" -> "['Alice', 'bacon', 'eggs', 'spam']
        
        for fooditem in range(1,len(line)): # NOTE: fooditem is an int
            if not(line[fooditem] in dict):       #if fooditem not in dict
                newList = []                         #create new list
                newList.append(line[0])              #append name to empty list 
                dict[line[fooditem]] = newList       #add list of names (value) to fooditem(key)
                #print("new:" + str(dict))
            else:
                existingList = dict[line[fooditem]]
                existingList.append(line[0])
                existingList.sort() #sorts list of names lexicographically
                dict.update({line[fooditem]: existingList}) 
                #print("existing:" + str(dict))
    
    
    result = sorted(dict.items()) #sort dict, returns tuple

    listConversion = []
    listConversion = list(result)         #convert tuple to list 
    resultList.append(listConversion)     #add list to resultList
    

for list in resultList: #list: [('ham', ['Joe', 'Sue']), ('spam', ['Joe'])]
    if (list):
        for element in list: # element: ('ham', ['Joe', 'Sue'])
            print(str(element[0]), end=" ") # element[0] == ham
            for names in element[1]:
                print(str(names), end=" ")
            print("\n", end="")
        print("")

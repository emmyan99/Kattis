
x = 1
report = ""

while(x != 0):
    x = int(input()) # no. of customers
    dict = {}

    for i in range(x): 
        line = input()
        line = line.split() # "Alice bacon eggs spam" -> "['Alice', 'bacon', 'eggs', 'spam']
        list = []
        for j in range(1,len(line)):     
            list.append(line[j])
            dict[line[0]] = list # {'Alice': ['bacon', 'eggs', 'spam']}
    
        for key, lists in dict.items():
            for fooditem in lists:
                print("report: " + report)

                if not report: # first iteration
                    report += fooditem + " " + str(key)
                else:
                    if not(str(fooditem) in report): # item is not in report
                        report += "\n" + fooditem + " " + str(key)
                    else:
                        None
                        #index = report.index(fooditem)
                        #print(index)

                
                
               



                    

                



    









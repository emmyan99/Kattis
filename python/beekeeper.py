def main():
    count = 0
    vowels = "aeiouy"

    while(count < 10):
        testCaseNo = int(input())
        count += 1
        output = []
        
        if testCaseNo == 0: break
        else: 
            while(testCaseNo > 0):
                dict = {}
                word = input()
                testCaseNo -= 1

                index = 0
                positions = []
                for char in word:
                    if vowels.find(char) > 0:
                        positions.append(index)
                        #print("vowelfiound")
                    else:
                        pass
                        print(char)
                    index += 1
                    #print(index)
                index = 0

                #print(positions)
                doubleCount = 0
                for i in positions:
                    for j in positions:
                        if j - i == 1:
                            #print(i, j)
                            doubleCount += 1
                #print(doubleCount)
                
                dict[word] = doubleCount
                #print(dict)


                


    
                    



#"beekeeper"
# index of vowels
# if two indexes are next to each other
# add count for each of these cases
# max wins
            




main()
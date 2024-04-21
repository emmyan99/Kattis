def main():
    count = 0
    vowels = "aeiouy"
    results = []

    while(count < 10):
        testCaseNo = int(input())
        count += 1
        
        if testCaseNo == 0: break
        else: 
            dict = {}
            doubleCounts = []
            while(testCaseNo > 0):
                word = input()
                testCaseNo -= 1

                index = 0
                positions = []
                for char in word:
                    if vowels.find(char) != -1:
                        positions.append(index)
                    else:
                        pass
                    index += 1

                doubleCount = 0
                for i in positions:
                    for j in positions:
                        if i - j == 1 and word[i] == word[j]:
                            doubleCount += 1
                doubleCounts.append(doubleCount)

                #word = key, doubleCount = value
                dict[doubleCount] = word
        #print(doubleCounts) 
        highestDoubleCount = max(doubleCounts)
        #print("highest: ", highestDoubleCount)
        results.append(dict[highestDoubleCount])
        #print(results)

    for x in results:
        print(x)
                    
#"beekeeper"
# index of vowels
# if two indexes are next to each other
# add count for each of these cases
# max wins

main()

def main():
    count = 0
    vowels = "aeiouy"

    while(count < 10):
        testCaseNo = int(input())
        count += 1
        if testCaseNo == 0: break
        else: 
            while(testCaseNo > 0):
                word = input()
                testCaseNo -= 1

                index = 0
                positions = []
                for char in word:
                    if vowels.find(char) > 0:
                        positions.append(index)
                    else:
                        pass
                    index += 1
                print(positions)

                double = 0
                for i in positions:
                    for j in positions:
                        if j - i == 1:
                            double += 1
                print(double)

                


    
                    



#"beekeeper"
# index of vowels
# if two indexes are next to each other
# add count for each of these cases
# max wins
            




main()
def main():
    count = 0
    vowels = ["a","e", "i", "o", "u", "y"]

    while(count < 10):
        testCaseNo = int(input())
        count += 1
        if testCaseNo == 0: break
        else: 
            while(testCaseNo > 0):
                word = input()
                testCaseNo -= 1

                positions = []
                for vowel in vowels:
                    positions.append(word.find(vowel))
                    print(positions)

                    indexes = []
                    for value in positions:
                        if value > 0:
                            indexes.index(value)
                    print(indexes)

    
                    



#"beekeeper"
# index of vowels
# if two indexes are next to each other
# add count for each of these cases
# max wins
            




main()
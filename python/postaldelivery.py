n, capacity = input().split()
n = int(n) # number of lines
capacity = int(capacity) # carrying capacity of truck
totalDistance = 0
print("number of lines:", n ,"\ncapacity:", capacity)

while n > 0:
    coord, numLetters = input().split()
    coord = int(coord) # location of delivery 
    numLetters = int(numLetters) # number of letters to delivery
    # take in all inputs at once instead
    # origin is location of the post office
    print("coord:", coord ,"\nletters to deliver:", numLetters)

    # needs to take into account next line in case both deliveries can be done at once?
    # maybe try turning it into a while loop instead, dependent on numLetters
    if numLetters < capacity: # if all letters fit in truck
        totalDistance += 2*abs(coord)
        print(totalDistance)
    else: # if only some letters fit
        numLetters =- capacity
        #lol what sssss


    n -= 1


# output: minmum total travel distance, including return to post office

n, capacity = input().split()
n = int(n) # number of lines
capacity = int(capacity) # carrying capacity of truck
totalDistance = 0

while n > 0:
    coord, numLetters = input().split()
    coord = int(coord) # location of delivery 
    numLetters = int(numLetters) # number of letters to delivery
    # origin is location of the post office


    if numLetters < capacity: # needs to take into account next line in case both deliveries can be done at once?
        totalDistance += 2*coord
        print(totalDistance)
    else: #
        print("placeholder")


    n -= 1


# output: minmum total travel distance, including return to post office

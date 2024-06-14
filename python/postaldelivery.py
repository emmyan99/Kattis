# origin is location of the post office
# input: first line contains two integers, n and c, where is n the number of delivery addresses on the route, 
# and c is the carrying capacity of the truck. Each of the following lines will contain two integers,
# the location of a delivery and the number of letters to deliver there
n, capacity = input().split()
n = int(n) # number of lines
capacity = int(capacity) # carrying capacity of truck
totalDistance = 0
print("number of lines:", n ,"\ncapacity:", capacity)
toDeliver = set() # leftover at office, tuples: (location, numLetters))
# ex. toDeliver.add((10, 40))

while n > 0:
    coord, numLetters = input().split()
    coord = int(coord) # location of delivery 
    numLetters = int(numLetters) # number of letters to delivery
    print("coord:", coord ,"\nletters to deliver:", numLetters)

    if len(toDeliver) == 0: # if there are no letters leftover at the office
        if numLetters < capacity: # if all letters fit in truck AND there are no leftovers at the office
            totalDistance += 2*abs(coord)
        else: # if only a portion of the letters fit
            totalDistance += 2*abs(coord)
            toDeliver.add((coord, (numLetters-capacity)))
    else: # if there are letters leftover at the office to consider
        print("you forgot letters at the office!!!")
        # logic to be added, check if letters can at office can be brought with on the way to another location

    # for debugging
    for i in toDeliver:
        print("letters at office:", i)
    print("total Distance so far:", totalDistance)

    n -= 1

# output: minmum total travel distance, including return to post office

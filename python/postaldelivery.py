# origin is location of the post office
# input: first line contains two integers, n and c, where is n the number of delivery addresses on the route, 
# and c is the carrying capacity of the truck. each of the following lines will contain two integers,
# the location of a delivery and the number of letters to deliver there

n, capacity = input().split()
n = int(n) # number of lines
capacity = int(capacity) # carrying capacity of truck
totalDistance = 0
print("number of lines:", n ,"\ncapacity:", capacity)
toDeliver = [] # leftover at office, tuples: (location, numLetters))
# ex. toDeliver.append((10, 40))

while n > 0:
    coord, numLetters = input().split()
    coord = int(coord) # location of delivery 
    numLetters = int(numLetters) # number of letters to delivery
    print("coord:", coord ,"\nletters to deliver:", numLetters)

    # first of all check if numLetters is larger than capacity and take action depending on this factor

    if len(toDeliver) == 0: # if there are no letters leftover at the office
        if numLetters < capacity: # if all letters fit in truck
            totalDistance += 2*abs(coord) # TODO: what if next set of letters can be brought on the same trip?
        else: # if only a portion of the letters fit
            totalDistance += 2*abs(coord)
            toDeliver.append((coord, (numLetters-capacity)))

    else: # if there are letters leftover at the office to consider
        if numLetters+(toDeliver[0])[1] < capacity and coord > (toDeliver[0])[0]: # if current letters and next fit in truck
            toDeliver = [] # empty
            totalDistance += 2*abs(coord)
        # deliver part of letters from office and current lettesr to their locations, leave a portion
        # if numLetters fills capacity, do not consider leftover office lettesr?

    # for debugging
    for i in toDeliver:
        print("letters at office:", i)
    print("total Distance so far:", totalDistance)

    n -= 1

# output: minmum total travel distance, including return to post office

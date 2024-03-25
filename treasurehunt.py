def main():
    row, col = input().split()
    row = int(row)
    col = int(col)

    mapsize = row*col
    startpoint = [0,0]
    treasurefound = False
    steps = 0

    firstAction = input()
    act0, act1 = splitActions(firstAction)
    (newpos, treasurefound, steps) = actionHandler(act0, startpoint, treasurefound, steps)
    (newpos, treasurefound, steps) = actionHandler(act1, newpos, treasurefound, steps)


    while((row-1) > 0):
        actions = input()
        act0, act1 = splitActions(actions)
        (newpos, treasurefound, steps) = actionHandler(act0, newpos, treasurefound, steps) 
        (newpos, treasurefound, steps) = actionHandler(act1, newpos, treasurefound, steps)
        row = row - 1

    if (newpos[0] > row or newpos[0] < 0 or newpos[1] > col or newpos[1] < 0):
        print("Out")
    elif(treasurefound == False):
        print("Lost")
    elif (treasurefound == True):
        print(steps)
 

def actionHandler(action, position, bool_, steps):
    steps = countSteps(steps, bool_)
    if (action == "T"):
        bool_ = True
    elif (action == "N"):
        position[1] -= 1
    elif (action == "S"):
        position[1] += 1
    elif (action == "W"):
        position[0] -= 1
    elif (action == "E"):
        position[0] += 1
    return (position, bool_, steps)


def countSteps(steps, bool_):
    if bool_ == False:
        steps += 1
    else:
        steps = steps
    return steps

def splitActions(actions):
    if len(actions) == 2:
        act0 = actions[0]
        act1 = actions[1]
    return act0, act1


main()



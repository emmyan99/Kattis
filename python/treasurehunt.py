#input line 1: R row, C col (1,200)
#R lines of input, C letters in each, each letter defines an action
#starting point at (0,0)

#N
#indicates a move to the previous row,

#S
#indicates a move to the next row,

#W
#indicates a move to the previous column,

#E
#indicates a move to the next column, and

#T
#indicates the location of the treasure.

#out of bounds - Out
#no treasure - print Lost
#Treasure - print amount of steps

def main():
    row, col = input().split()
    row = int(row)
    col = int(col)
    count = int(row)

    newpos = [0,0]
    treasurefound = False
    steps = 0
    gameover = False


    while(count > 0): 
        actions = list(input()) # splits actions into a list of chars, col chars long
        for action in actions:
            if (action == "T") and not treasurefound:
                treasurefound = True
                steps += 1
            else:
                if(treasurefound == False):
                    steps +=1
                (newpos) = actionHandler(action, newpos)
                if (newpos[0] > (row-1) or newpos[0] < 0 or newpos[1] > (col-1) or newpos[1] < 0):
                    gameover = True
        count -= 1

    if gameover:
        print("Out")
    elif treasurefound:
        print(steps)
    else:
        print("Lost")



def actionHandler(action, position): #(row,col)
    if (action == "N"):
        position[0] -= 1
    elif (action == "S"):
        position[0] += 1
    elif (action == "W"):
        position[1] -= 1
    elif (action == "E"):
        position[1] += 1
    return (position)



main()



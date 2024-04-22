x = int(input())
playerLost = 0
firstWord = True
words = set()

#if x is even, player 1 only plays on even turns
player1even = x%2 ==0

while x > 0:
    word = input()

    if firstWord:
        last = word[-1]
        firstWord = False
    else:
        if word[0] == last and not(word in words):
            last = word[-1]
        else:
            if player1even and x%2 == 0:
                playerLost = 1
            elif player1even and x%2 != 0:
                playerLost = 2
            elif not(player1even) and x%2 == 0:
                playerLost = 2
            elif not(player1even) and x%2 != 0:
                playerLost = 1
            break
    x -= 1
    words.add(word)


if playerLost == 0:
    print("Fair Game")
else:
    print("Player", str(playerLost) ,"lost")

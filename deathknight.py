x = int(input())

wins = 0

for y in range(x):
    moves = input()

    if (moves.find("CD") == -1):
        wins += 1

print(wins)

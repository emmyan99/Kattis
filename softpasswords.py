S = input()
P = input()

if S == P:
    print("Yes")
elif S[0].isnumeric() and S[1:] == P: 
    print("Yes")
elif S[-1].isnumeric() and S[:-1] == P:
    print("Yes")
elif S.swapcase() == P: 
    print("Yes")
else:
    print("No")
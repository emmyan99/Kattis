phonenumba = int(input())

#if first 3 # in phonenumba are 3, print 1
#if not, print 0

result = []

for char in str(phonenumba)[0 : 3 : 1]:    #string [starting index : ending index : step value]
    if char == "5":
        result.append(True)
    else:
        break

if result == [True, True, True]:
    print(1)
else:
    print(0)

#phonenumba = str(phonenumba)
#asd = True

#for i in range(0, 3):
#    if phonenumba[i] == '5':
#        continue
#    else:
#        asd = False

#if asd:
#    print(1)
#else:
#    print(0)
S = input()
alphabet = []
number = 0

for s in S:
    if "A" <= s <= "Z":
        alphabet.append(s)
    else:
        number += int(s)

alphabet.sort()

for a in alphabet:
    print(a, end='')
print(number)

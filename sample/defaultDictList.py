from collections import defaultdict

dftdict = defaultdict(list)

for i in range(3):
    dftdict[i].append(i)

print(dftdict)
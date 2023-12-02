from collections import defaultdict

intdict = defaultdict(int)

X = [1,2,3,4,5,1,1,3,4,5]

for i in X:

#The default value is 0 so there is no need to enter the key first

    intdict[i] += 1

print(intdict)
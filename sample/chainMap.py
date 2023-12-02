from collections import ChainMap

x1 = {'a': 0, 'b': 1}
x2 = {'c':2,'d':3}
x3 = {'e':4,'f':5}

chainmap = ChainMap(x1,x2,x3)

print(chainmap)
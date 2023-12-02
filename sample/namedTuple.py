from collections import namedtuple

band = namedtuple('Country',['name','capital','famousband'])

val = band("south korea","Seoul","BTS")
print(val)
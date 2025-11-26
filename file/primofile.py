f = open("caratteri", "w")

import random
import string

for i in range(1000):
    f.write ("".join(random.choices(string.ascii_letters)) + "\n")

f.close()

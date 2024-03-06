fruist = list()

fruist.append('Apple')
fruist.append('kiwi')
fruist.append('banana')
print(fruist)
print(len(fruist))
some_fru = fruist.pop()
print(fruist)

del fruist[0]
print(fruist)

import random

random_numbers = []
for i in range(10):
    random_numbers.append(random.randint(0,15))
print(random_numbers)
order = sorted(random_numbers)
print(order)
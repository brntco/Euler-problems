from itertools import permutations
cube = 20
lst=list(("v"*cube)+("h"*cube))
print(len(list(permutations(lst))))

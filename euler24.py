
"""
A brute force approach.
no need to check the permutations of the first nine digits.
We know that index number (9!) but you are still left with some 1.7 billion numbers to check.
Obviously one needs to find a quicker way than this, but itertools seemed a bit like cheating.
"""
count = 362880
lowcheck = 1000000000
#print(len(set(str(lowcheck))))
hicheck = 1023456789
while count <= 999999:
  if len(set(str(lowcheck))) == 10:
    count += 1
    check += 1
check -= 1
print(check)
print(count)

#returns: 2783915460


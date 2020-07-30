# numbers > 28123 can all be written as sum of abundant numbers.
# sum of numbers that can't be written as sum of abundant numbers
# abundant number is when sum of divisors is greater than number
# Find all abundant numbers under limit (largest - smallest  = 28112)
# Make a set of all numbers that are sums of abundant numbers ("abunsummed"):
# Subtract sum of all numbers able to be added

def abuncheck(n): #  create list of divisors of n from a given number, add them together and check if they are greater than n.
    p = [1]
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            p.extend([i, int(n/i)])
    if sum(set(p)) > n:
        return n
    else:
        return False


abunlist = []
abunsum = []
for x in range(28123):
    if abuncheck(x):
        abunlist.append(abuncheck(x))
for each in range(len(abunlist)):
    for every in range(each, len(abunlist)):
        if (abunlist[each] + abunlist[every]) <= 28123:
            abunsum.append(abunlist[each] + abunlist[every])
abunset = set(abunsum)
#print(sum(abunset) == sum(abunsum))
# print(sum(abunset))
# print(sum(range(28123)))
nonabunsummed = sum(range(28124)) - sum(abunset)
# for y in range(28123):
#     if y not in abunsum:
#         nonabunsummed += y
#
print(nonabunsummed)

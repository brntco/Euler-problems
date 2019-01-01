def divnsum(n):
    p = [1]
    for i in range(2, int(n**(1/2)+1)):
        if n % i == 0:
            p.extend([i, int(n/i)])
    return (sum(set(p)))


param = 10000
amicable=[]

for b in range(2, param):
    if not b == divnsum(b): #remove narcissistic numbers
        if divnsum(divnsum(b)) == b:
            amicable.extend([b, divnsum(b)])

print(sum(set(amicable)))


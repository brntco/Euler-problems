import timeit
start = timeit.default_timer()

x = 1
trisum = 1
while True:
    divisors=[]
    x+=1
    trisum += x
    for p in range(1, int((trisum**.5) + 1)):
        if trisum%p==0:
            divisors.extend([p, trisum/p])
    if len(set(divisors))>=500:
        print(trisum)
        break

stop = timeit.default_timer()
print(stop-start)
 

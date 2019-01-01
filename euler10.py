import timeit

start = timeit.default_timer()

list_target = int(2000000**(1/2))
print(list_target)
check = 11
prm = [2, 3, 5, 7]
while check < list_target:
    p = True
    for x in prm:
        if check%x == 0:
            p = False
    if p:
        prm.append(check)
    check += 2
answer = sum(prm)

target = 2000000
checker = list_target
while checker < target:
    p = True
    for x in prm:
        if checker%x == 0:
            p = False
    if p:
        answer += checker
    checker += 2
print(answer)

stop = timeit.default_timer()
m1 = (stop-start)
print(m1)

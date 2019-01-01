list_target = 10003
prime_list= [2]
check = 3
while len(prime_list) < list_target:
    p = True
    for x in prime_list:
        if check%x == 0:
            p = False
    if p == True:
            prime_list.append(check)
    check += 2
print(prime_list[10000])

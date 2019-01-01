y = 600851475143
#s = round(y**1/2)
#print(s)
prime_list= [2, 3]
check = 5
while check < y:
    p = True
    for x in prime_list:
        if check % x == 0:
            p = False
    if p == True:
        prime_list.append(check)
        #print(check)
        if y % check == 0:
            print(check)
    check += 2


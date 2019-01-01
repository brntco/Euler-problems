i = 1
h = 2
fib = [i, h]
while True:
    i = i+h
    #print(i)
    h = h+i
    #print(h)
    if h >= 4000000:
            break
    fib.append(i)
    fib.append(h)
def evens(fib):
    return [x for x in fib if x % 2 == 0]
print(sum(evens(fib)))


    

fib = 1
fib2 = 1
count = 2
while len(list(str(fib))) <= 999 and len(list(str(fib2))) <= 999:
    fib = fib + fib2
    count += 1
    fib2 = fib2 + fib
    count += 1
print(count)
print(len(str(fib)))
print(len(str(fib2)))

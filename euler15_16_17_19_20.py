# Euler 15
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


print((factorial(40)) / (factorial(20) ** 2))

# Euler 16
big = list(str(2 ** 1000))
print(sum(int(i) for i in big))

# euler 17
f9 = [3, 3, 5, 4, 4, 3, 5, 5, 4]
f10s = [6, 6, 5, 5, 5, 7, 6, 6]
teens = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
print((sum(f9) * 190) + (sum(f10s) * 100) + (sum(teens) * 10) + (3 * 891) + (7 * 900) + 11)

#Euler 19

m1 = 31
m2 = 30
m3 = 28
m4 = 29
year = [m1, m3, m1, m2, m1, m2, m1, m1, m2, m1, m2, m1]
lyear = [m1, m4, m1, m2, m1, m2, m1, m1, m2, m1, m2, m1]
time = 0
sundays = 0
for i in lyear:
    time += i
    if time % 7 == 0:
        sundays += 1
time %= 7
sundays = 0
century = (year * 3 + lyear) * 25
for i in century:
    time += i
    if time % 7 == 0:
        sundays += 1
print(sundays)


# euler20
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)


lst = (list(str(factorial(100))))
print(sum(int(i) for i in lst))
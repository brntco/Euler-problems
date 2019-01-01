potty = list()
for sq in range(1,101):
    potty.append(sq**2)
big_potty = sum(potty)
#print(potty)
#print("et voila")
#print(big_potty)
pull_ups = sum(list(range(1,101)))**2
print(big_potty - pull_ups)

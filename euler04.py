largest = 0
for i in range(100,1000):
    for j in range(i+1,1000):
        if str(j*i) == str(j*i) [::-1]:
            if i*j > largest:
                largest = i*j
print(largest)
                        
        
   
        
    
    

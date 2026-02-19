def aval(n):
    avaal = True
    for i in range (2 , int(n**0.5)+1):
        if (n % i == 0):
            avaal = False
            break
    return avaal
aval_count = 0   
akharin_adad_aval = 0 
for i in range (1 , 10001):
    if aval(i):
        aval_count = aval_count + 1
        akharin_adad_aval = (i)
        print (i)
print ("")
print ("we had" , aval_count , "aval_number")        
print ("akharin adad aval hastesh" , akharin_adad_aval)
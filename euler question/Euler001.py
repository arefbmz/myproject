# Answer to Euler's first question
def adad(n):
    if (n % 3 == 0 or n % 5 == 0):
        return True
    else:
        return False
sum = 0
for i in range (1 , 1000):
    if adad(i) :
        sum = sum + i

print (sum)
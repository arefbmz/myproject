name1 = input("please write your name number 1 : ")
birth_year1 = int(input("please write your birth year number 1 : "))
name2 = input("please write your name number 2 : ")
birth_year2 = int(input("please write your birth year number 2 : "))
current_year = 1397
age1 = current_year - birth_year1
age2 = current_year - birth_year2
print("Hello %s. You are %i years old" % (name1 , age1) , "\n" , "Hello %s. You are %i years old" % (name2 , age2))
bigger_age = 0
if age1 > age2 :
    bigger_age = age1 - age2
    print("%s is %i years older than %s" %(name1 , bigger_age , name2))
    
elif age1 < age2 :
    bigger_age = age2 - age1
    print("%s is %i years older than %s" %(name2 , bigger_age , name1))

else:
    print("%s and %s are the same age" %(name1 , name2))

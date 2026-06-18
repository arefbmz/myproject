import random

a, b = [1, 99]
new1 = 0
new2 = 0
answer = random.randint(a, b)
print(answer)
while True:
    pcguess = input("ok / s / l : ")
    if pcguess == "ok":
        print("pc can guess and win")
        break
    elif pcguess == "s":
        b = answer
        answer = random.randint(a, b)
        print(answer)
    elif pcguess == "l":
        a = answer
        answer = random.randint(a, b)
        print(answer)
  
# INSERT_YOUR_CODE
# بعد از پایان چرخه while تعداد تلاشها را چاپ کن
print(f"you win after {new1} tries")
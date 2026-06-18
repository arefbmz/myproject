name = input("please write your name: ")
time = int(input("please write how much hour to work per day: "))
fee = int(input("please write how much fee to work per hour: "))

more_work = 0
more_time = time - 12
all_money = time * fee


def payment(time, fee):
    if time > 12:
        more_work = 8 * more_time
        full_day = all_money + more_work
        return full_day
    else:
        return all_money


print("your payment is : ", payment(time, fee), "$")

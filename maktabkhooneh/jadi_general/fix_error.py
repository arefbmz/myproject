def divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("b cant be 0")
        return None
    finally:
        print("program run successful")

while True:
    try:
        # مرحله 1: گرفتن ورودی‌ها و چک کردن ValueError
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        
        # مرحله 2: فراخوانی تابع و چک کردن خروجی
        res = divide(num1, num2)
        
        if res is not None:
            print("Result:", res)
            break  # اگر تقسیم موفق بود (None نبود)، از حلقه خارج شو
        else:
            print("Please try again with valid numbers.")
            
    except ValueError:
        print("error for write str no int")
        # در صورت حروف وارد کردن، حلقه دوباره تکرار می‌شود

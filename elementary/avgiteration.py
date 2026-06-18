sum = 0
totall = 0

while True:
    numbers = int(input("please write the number(for end write -1): "))
    if numbers == -1:
        break

    sum += numbers
    totall += 1

if totall > 0:
    average = sum / totall
    print("average: ", average)
else:

    print("Error , no numbers entered. ")

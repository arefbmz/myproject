# Answer to Euler's sign up question
def total():
    sum = 0

    for i in range(1, 954001):
        if i % 2 != 0:
            sum = sum + i * i
    return sum


answer = total()
print(answer)

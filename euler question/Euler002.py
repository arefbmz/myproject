# Answer to Euler's question 2
def fiboeven(n):
    if n % 2 == 0:
        return True
    else:
        return False


first = 1
second = 2

sum = 0

while first < 4 * 10**6:
    if fiboeven(first):
        sum = sum + first
    new = first + second
    first = second
    second = new

print(sum)

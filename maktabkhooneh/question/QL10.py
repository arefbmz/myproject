fruit_list1 = ["apple", "berry", "cherry", "papaya"]
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]

fruit_list2[0] = "guava"
fruit_list3[1] = "kiwi"

sum = 0

for Is in (fruit_list1, fruit_list2, fruit_list3):
    if Is[0] == "guava":
        sum += 1
    if Is[1] == "kiwi":
        sum += 20
print(sum)

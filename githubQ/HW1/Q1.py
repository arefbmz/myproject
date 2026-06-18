sms_sara = input("Enter the written message: ").rstrip("\n")
sum_words = len(sms_sara)
# count = 0
blocks = sum_words // 24
cost = (blocks * 274) + 100
# for i in sms_sara:
# count += 1
# print(count , i )
print("len sms_sara is : %i and Cost sms_sara is : %i" % (len(sms_sara), cost))

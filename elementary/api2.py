import requests


# import json
def inform_aref(price):
    API_Key = "517A5848667873522F6335395932395771517865546659414D6166736169427139394952626F334A7A46343D"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % API_Key
    payload = {"receptor": "00000000000", "message": "price is as low as %i" % price}
    r = requests.post(url, data=payload)
    print(r)
    # print(r.status_code)
    # print(r.text)
    # print("Kavenegar status:", r.status_code) //برای دیباگ
    # print("Kavenegar body:", r.text) //برای دیباگ

    # print (" hi there. time is good for buy")


time_to_buy = 60000
r = requests.get(
    "https://api.coinbase.com/v2/prices/BTC-USD/buy"
)  # , proxies={"http": "MTProto://85.133.194.201:8443"})
# print("Coinbase status:", r.status_code)//برای دیباگ
# print("Coinbase body:", r.text)//برای دیباگ
# print (json.dumps(r.json(), indent=4))
price = float(r.json()["data"]["amount"])
# print("Parsed price:", price) //برای دیباگ
# print("at this moment, bitcoinn is %i usd " % price )
if price < time_to_buy:

    # smsresult = requests.get(" . . . ")
    # print (time_to_buy)
    inform_aref(price)
# else:
# print("its not time to buy yet.")

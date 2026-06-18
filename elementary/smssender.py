import requests

filename = "/home/xxxx/desktop/phones"
text = """ Relax its send soon 
sorry for late 
"""


def readphones(filename):  # TODO: read the phone numbers from the file name
    with open(filename) as f:
        content = (
            f.readlines()
        )  # you may also want to remove whitespace charecters live `/n` at the emd of each line
    content = [x.strip() for x in content]
    return content


def send_sms(number, text):  # TODO: send sms and return result
    API_Key = "517A5848667873522F6335395932395771517865546659414D6166736169427139394952626F334A7A46343D"
    url = "https://api.kavenegar.com/v1/%s/sms/send.json" % (API_Key)

    data = {"receptor": number, "message": text}
    r = requests.post(url, data=data)
    return r.ok


phones = readphones(filename)
for phone in phones:
    if not send_sms(phone, text):
        print(phone)

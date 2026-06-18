name = input(" please write your name : ")
while True:
    sath_shoma = input(" sath shoma : ")
    if sath_shoma == "0":
        print("sath shoma mogadamati ast")
        break
    elif sath_shoma == "0.25 ":
        print("sath shoma motevaset ast")
        break
    elif sath_shoma == "0.5":
        print("sath shoma awali ast")
        break
    elif sath_shoma == "0.75":
        print("sath shoma pishrafte ast")
        break
    elif sath_shoma == "1":
        print("sath shoma herfiye ast")
        break
    else:
        if sath_shoma != ("0 , 0.25 , 0.5 , 0.75 , 1"):
            print("ma chenin sathi nadarim")
            break

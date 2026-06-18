from docx import Document

numbersdone = 0
numbersoffixes = 0
doc = Document("/temp/xxxxx/doc.docx")
for para in doc.paragraghs:
    newtxt = ""
    for char in para.text:
        if char in "1234567890":
            numbersoffixes += 1
            if numbersdone == 0:
                newtxt += char
                numbersdone += 1
            else:
                newtxt = (
                    newtxt[: -1 * numbersdone] + char + newtxt[-1 * numbersoffixes :]
                )
                numbersdone += 1
        else:
            newtxt += char
            numbersdone = 0

    para.text = newtxt
print("in total i fixed ", numbersoffixes)
doc.save("/tmp/xxxxx/dox.doxs")

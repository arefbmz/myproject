rec = {"name": "python programmer", "age": "20", "addr": "NJ", "country": "USA"}
id1 = id(rec)
del rec
rec = {"name": "python programmer", "age": "20", "addr": "NJ", "country": "USA"}
id2 = id(rec)
print(id1 == id2)

string = "yes we can , we win , we freedom and now we should make all destroyed history and return my biggest wonderful"

counter = dict()
for letter in string:
    counter[letter] = counter.get(letter, 0) + 1
    # if letter in counter:
    # counter[letter] += 1
    # else:
    # counter[letter] = 1

for this_one in list(counter.keys()):
    print("%s appeared %s time" % (this_one, counter[this_one]))

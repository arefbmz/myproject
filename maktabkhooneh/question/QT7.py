i = [1,2,3]

init_tuple = ('python',) * (i.__len__() - i[::-1][0])

print(init_tuple)
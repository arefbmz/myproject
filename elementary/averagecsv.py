import csv
from statistics import mean

with open("/home/arefbmz/myproject/elementary/grades.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        these_grades = list()
        for grade in row[1:]:
            these_grades.append(int(grade))
        print("average of %s is %5.2f " % (name, mean(these_grades)))

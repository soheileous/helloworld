import csv
from statistics import mean
from unittest.util import sorted_list_difference    
with open ('d:/python/grades.csv') as fin:
    reader = csv.reader(fin)
    for row in reader:
        students_and_grades = {row[0]:row[1:]}
        name = row[0]
        introw = []
        for grade in row[1:]:
            introw.append(int(grade))

        avg_students = mean(introw)
        average = {name:avg_students}
        #sort_student_averages = sorted(average.items(), key = lambda x:x[1], reverse = False) | ba'dan bebinam chera kar nemikone :(
        sort_1 = list(average.values())
        sort_student_averages=[]

        for a in sort_1:
            print (a, type(a))


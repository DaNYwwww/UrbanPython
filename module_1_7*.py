students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students_list=list(students)
average_grades={}
for students in students_list:
    students_grades = grades[students_list.index(students)]
    average_grade = sum(students_grades) / len(students_grades)
    average_grades[students] = average_grade
print(average_grades)

grades=[[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students={'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_1=sorted(students) # Отсортировал в алфавитном порядке
grades_1=sum(grades [0])/(len(grades[0]))
grades_2=sum(grades [1])/(len(grades[1]))
grades_3=sum(grades [2])/(len(grades[2]))
grades_4=sum(grades [3])/(len(grades[3]))
grades_5=sum(grades [4])/(len(grades[4]))
average_rating=dict(zip(students_1, grades_1,grades_2,grades_3,grades_4,grades_5))

print(average_rating)


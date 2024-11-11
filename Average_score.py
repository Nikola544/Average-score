grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Джонни', 'Бильбо', 'Стив', 'Гендрик', 'Аарон'}
sorted_students = sorted(students)
average_grades = {name: sum(grades[i]) / len(grades[i]) for i, name in enumerate(sorted_students)}
print(average_grades)
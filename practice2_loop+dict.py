# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]
student_dict = {}

for student in students:
    
    name = student['first_name']
    
    if student_dict.get(name) == None:
        student_dict[name] = 1
    else:
        student_dict[name] += 1

for key, value in student_dict.items():
    print('{} : {}'.format(key, value))

print('______\n')




# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
# Пример вывода:
# Самое частое имя среди учеников: Маша

students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
students_dict = {}
for student in students:
    name=student['first_name']
    if not students_dict.get(name):
        students_dict[name] = 1
    else:
        students_dict[name] += 1

high_val  = max(students_dict.values())       
most_name_index = list(students_dict.values()).index(high_val)
print('Most popular name is {}'.format(list(students_dict.keys())[most_name_index]))
print('______\n')
# ???



# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
school_students = [
  [  # это – первый класс
    {'first_name': 'Вася'},
    {'first_name': 'Вася'},
  ],
  [  # это – второй класс
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
  ]
]
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

class_count = 0

for school_class in school_students:
    students_dict = {}
    class_count+=1

    for students in school_class:
        name=students['first_name']
        if not students_dict.get(name):
            students_dict[name]=1
        else:
            students_dict[name]+=1

    high_val  = max(students_dict.values())       
    most_name_index = list(students_dict.values()).index(high_val)
    print('Most popular name in class {} is {}'.format(class_count, list(students_dict.keys())[most_name_index]))    

print('______\n')

# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

#сделать листы с именами и проверять по ним

for school_class in school:
    class_name = school_class['class']
    count_male   = 0
    count_female = 0
    
    for student in school_class['students']:
        if not is_male[student['first_name']]:
            count_female+=1
        if is_male[student['first_name']]:
            count_male+=1

    print('In class {} is {} females and {} males'.format(class_name, count_female, count_male))

print('______\n')

# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков.
school = [
  {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
  {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
  'Маша': False,
  'Оля': False,
  'Олег': True,
  'Миша': True,
}
# ???

# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a
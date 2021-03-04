# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Петя'},
]

from collections import Counter

name_list = []

for student in students:
    name_list.append(student['first_name'])

names = Counter(name_list)

for name in names:
    print(f'{name} : {names[name]}')

print('\n______________\n')


# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя.
students = [
  {'first_name': 'Вася'},
  {'first_name': 'Петя'},
  {'first_name': 'Маша'},
  {'first_name': 'Маша'},
  {'first_name': 'Оля'},
]
# Пример вывода:
# Самое частое имя среди учеников: Маша

from collections import Counter

#<<<<<<<<<<<<<<<<<<<<<<< Правильно ли использовать такую коснтрукцию? 
name_list = [i.get('first_name') for i in students]

names = Counter(name_list)
max_val = max(names, key=names.get)
#max_val = names.most_common(1)
print(f'most common name is {max_val}')
print('\n______________\n')


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
# ???

# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

from collections import Counter

counter = 0

for school_class in school_students:
  counter+=1
  name_list = []

  for student in school_class:
      name_list.append(student['first_name'])

  names = Counter(name_list)
  max_val = max(names, key=names.get)
  print(f'most common name in class {counter} is {max_val}')

#<<<<<<<<<<<<<<<<<<<<<<< Возможно ли использовать метод nmost_common()? Если да, то как? 
#max_val = names.most_common(1)

print('\n______________\n')


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
# ???

# Пример вывода:
# В классе 2a 2 девочки и 0 мальчика.
# В классе 3c 0 девочки и 2 мальчика.

for school_class in school:
  class_name = school_class['class']
  female = 0
  male = 0

  for student in school_class['students']:
    name = student['first_name']
    if name in is_male.keys():
      if not is_male[name]:
        female+=1
      else:
        male+=1
    else:
      print(f'{name} is not define')

  print(f'there is {female} females and {male} males in {class_name} class')
print('\n______________\n')

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
school_dict = {}
male_dict   = {}
female_dict = {}


#<<<<<<<<<<<<<<<<<<<<<<< Можно ли описать цикл ниже проще? 
for school_class in school:
  class_name = school_class['class']
  female = 0
  male = 0

  for student in school_class['students']:
    name = student['first_name']
    if name in is_male.keys():
      if not is_male[name]:
        female+=1
      else:
        male+=1
    else:
      print(f'{name} is not define')
      
    male_dict[class_name] = male
    female_dict[class_name] = female

max_males   = max(male_dict, key=male_dict.get)
max_females = max(female_dict, key=female_dict.get)

print(f'There more boys in {max_males} class')
print(f'There more girls in {max_females} class')
print('\n______________\n')
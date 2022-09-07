# Задача №2 по расчету периметров и площадей геометрических фигур
print('Задача №2')
square = int(input('Введите длину стороны квадрата: '))
if square <= 0:
  print('Длина стороны квадрата должна быть больше 0!')
else:
  print('Периметр: ', square * 4)
  print('Площадь: ', square * square)

lenght = int(input('Введите длину прямоугольника: '))
width = int(input('Введите ширину прямоугольника: '))
if lenght <= 0:
  print('Длина прямоугольника должна быть больше 0!')
elif width <= 0:
  print('Ширина прямоугольника должна быть больше 0!')
else:
  print('Периметр: ', (lenght + width) * 2)
  print('Площадь: ', lenght * width)

# Задача №3 по расчету остатка заработной платы
print('Задача №3')
salary = int(input('Введите вашу заработную плату: '))
mortgage = int(input('Введите, какой процент(%) уходит на ипотеку: '))
life = int(input('Введите, какой процент(%) уходит на жизнь: '))

mortgage = (mortgage * salary / 100) * 12
life = (life * salary / 100) * 12
accumulation = (salary * 12) - mortgage - life
print('На ипотеку было потрачено: ', mortgage, 'рублей')
print('Было накоплено: ', accumulation, 'рублей')
month = input('Введите месяц: ')
day = int(input('Введите число: '))
month = month.lower()

if month == 'январь':
  month = 1
elif month == 'февраль':
  month = 2
elif month == 'март':
  month = 3
elif month == 'апрель':
  month = 4
elif month == 'май':
  month = 5
elif month == 'июнь':
  month = 6
elif month == 'июль':
  month = 7
elif month == 'август':
  month = 8
elif month == 'сентябрь':
  month = 9
elif month == 'октябрь':
  month = 10
elif month == 'ноябрь':
  month = 11
elif month == 'декабрь':
  month = 12
else:
  print('Вы ввели несуществующий месяц!')
  raise SystemExit('error month name input!')

if (day >=  21 and day  <=  31 and month  ==  3) or (month  ==  4 and day  >=  1 and day  <=  19):
  print("Знак зодиака: Овен")
elif (day >= 20 and day <= 30 and month == 4) or (month == 5 and day >= 1 and day <= 20):
  print("Знак зодиака: Телец")
elif (day >= 21 and day <= 31 and month == 5) or (month == 6 and day >= 1 and day <= 21):
  print("Знак зодиака: Близнецы")
elif (day >= 22 and day <= 30 and month == 6) or (month == 7 and day >= 1 and day <= 22):
  print("Знак зодиака: Рак")
elif (day >= 23 and day <= 31 and month == 7) or (month == 8 and day >= 1 and day <= 22):
  print("Знак зодиака: Лев")
elif (day >= 23 and day <= 31 and month == 8) or (month == 9 and day >= 1 and day <= 22):
  print("Знак зодиака: Дева")
elif (day >= 23 and day <= 30 and month == 9) or (month == 10 and day >= 1 and day <= 23):
  print("Знак зодиака: Весы")
elif (day >= 24 and day <= 31 and month == 10) or (month == 11 and day >= 1 and day <= 22):
  print("Знак зодиака: Скорпион")
elif (day >= 23 and day <= 30 and month == 11) or (month == 12 and day >= 1 and day <= 21):
  print("Знак зодиака: Стрелец")
elif (day >= 22 and day <= 31 and month == 12) or (month == 1 and day >= 1 and day <= 20):
  print("Знак зодиака: Козерог")
elif (day >= 21 and day <= 31 and month == 1) or (month == 2 and day >= 1 and day <= 18):
  print("Знак зодиака: Водолей")
elif (day >= 19 and day <= 29 and month == 2) or (month == 3 and day >= 1 and day <= 20):
  print("Знак зодиака: Рыбы")
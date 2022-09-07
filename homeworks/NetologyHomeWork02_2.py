height = 182
age = 17

if 18 < age < 27:
    if height < 170:
        print('В танкисты')
    elif height < 180:
        print('На флот')
    elif height < 200:
        print('в десантники')
    else:
        print('В другие войска')
else:
    print('Непризывной возраст!')

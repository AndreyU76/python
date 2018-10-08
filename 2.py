 // Удовиченко Андрей
age = int(input('Укажите ваш возраст: '))
if age < 18:
    print('Пользование данным ресурсом только с 18 лет !!!')
    access = False
else:
    print('Доступ разрешен')
    access = True

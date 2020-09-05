a = 1

while a==1:
    nmbs = input('Пожалуйста, введите числа через запятую:')

    if nmbs.find(","):
        formrray = nmbs.split(',')

        array = map(int, formrray)

        print("Список чисел: ", list(array))
        print("Кортеж из чисел: ", tuple(list(array)))

    else:
        print("В введеных вами числах не хватает запятых для их перечисления. Попытайтесь ещё раз;-(")



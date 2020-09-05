def threeD(figure):
    n = int(figure)
    nn = int(figure * 2)
    nnn = int(figure * 3)

    return n+nn+nnn

n = input('Введите целое число: ')
print("Результат трехмёрного сложения: ", threeD(n))
     
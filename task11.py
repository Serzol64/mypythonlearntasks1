import random

fa = []
for figure in range(1,10):
    random.seed(figure) #На основе получаемого итератора настраивается генератор случайных чисел
    fa.append(random.random())
print('Первый элемент:', fa[0])
print('Последний элемент:', fa[-1])
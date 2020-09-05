dd = {
    'Russia': 4102,
    'Belarus': 128,
    'China': 67,
    'United States': 1729,
    'Canada': 156
} #Словарь на основе текущих данных посещаемости сайта одного НКО за этот год

dataset = [list(dd.items()),list(dd.keys())]

dataset[0].sort(key=lambda i: i[1])

print('Down contries:') #Топ-5 отстающих стран посещаемости 
for i in dataset[0]:
    print(i[0],':',i[1])
print(' ')
dataset[1].sort()

print('Activity contries:') #Топ-5 активных стран посещаемости
for i in dataset[1]:
    print(i,':',dd[i])
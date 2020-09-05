a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newlist = []

for input in a:
    #Внутри этого цикла формируется цикл вывода, в соответствии с которым будет сформирован единый список.
    for output in b:
        if output == input:
            newlist.append(input)
print('Main math array:')
print(list(newlist))
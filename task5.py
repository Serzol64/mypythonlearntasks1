my_dict = {'a':500, 'b':5874, 'c': 560,'d':400, 'e':5874, 'f': 20}

print('Maximal keys:')
print([k for k,v in my_dict.items() if v == max(my_dict.values())])
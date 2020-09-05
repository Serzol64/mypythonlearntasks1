import os

print("Список файлов в текущей директории:")
for root, dirs, files in os.walk("."):  
    for filename in files:
        print(filename)
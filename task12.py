storage = ["index.html","config","temp","elsafrost.png","saratov.jpg","lock","robots.txt","message.cs","liza.aspx","girls.php","No Surprises.mp3","LinkinParkLiveMSK2011.mp4"]

def getfileextension(filename):
    fn = filename.split(".")
    if len(fn) < 2:
        print("Расширение файла не определено")
    else:
        print("Расширение получаемого имени файла:", fn[-1])
for query in storage:
    getfileextension(query) #Получая доступ к массиву файлового хранилища, она определяет и выводит расширения файлов


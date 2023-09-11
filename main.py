import requests
import pandas
import sys
import os

if not os.path.isfile("lab_pi_101.xlsx"):
    print("Файл не существует в текущей директории. Необходимо скачать.")
#На этом этапе происходит скачивание файла через библиотеку requests
    try:
        urlToExcelFile = 'https://drive.google.com/uc?export=download&id=1Bo5Oili5dAvWDSzAZXjzgjS71IrmLWun'
        workingUrlForDownloadingFile = requests.get(urlToExcelFile)
    except:
        print("Скачивание файла невозможно. Некорректная ссылка или отсуствует интернет-соединение.")
        sys.exit()

    try:  
        with open('lab_pi_101.xlsx', 'wb') as f: 
            f.write(workingUrlForDownloadingFile.content)
    except:
        print("Файл на сервере был переименован или имеет другой формат, отличный от xlsx! Проверьте название файла и запустите программу заново!")
        sys.exit()
#Когда файл скачан или он уже найден в директории, приступаем к самой работе с файлом
print("Файл найден в директории проекта!")
try:
    studentsMarksFGS = pandas.read_excel('lab_pi_101.xlsx') #читает Excel-файл
except:
    print("Не удаётся открыть файл!")
    sys.exit()
    
choosedGroup = str(input("Введите название группы:"))
marksChoosedGroup = len(studentsMarksFGS[studentsMarksFGS['Группа'] == choosedGroup])
if marksChoosedGroup == 0:
    print("Такой группы не существует")
    sys.exit()

marksCount = studentsMarksFGS.count()[0] #по умолчанию возвращает количество значений вдоль каждого столбца
studentsChoosedGroup = pandas.DataFrame(studentsMarksFGS[studentsMarksFGS['Группа'] == choosedGroup])
personalIDStudentsGroup = studentsChoosedGroup['Личный номер студента'].unique()
countStudentsChoosedGroup = len(studentsChoosedGroup['Личный номер студента'].unique())
print("В исходном датасете содержалось", marksCount, "оценок, из них ", marksChoosedGroup, "оценок относятся к группе", choosedGroup, "\nВ датасете находятся оценки", countStudentsChoosedGroup, "студентов со следующими личными номерами:", personalIDStudentsGroup, "\nИспользуемые формы контроля:", studentsChoosedGroup['Уровень контроля'].unique(), "\nДанные представлены по следующим учебным годам:", studentsChoosedGroup['Год'].unique())






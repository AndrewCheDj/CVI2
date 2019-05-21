import os
import xlrd

# выбор директории для работы
files = os.listdir('E:\code\Cvi\Cvi')
for file in files:
    # печать названий файлов
    print (file)
# печать названий файлов списком
print (files)

num = len(files) # количество файлов

# открытие файла excel, в []-кавычках номер файла excel

for i in range (num): # цикл открытия всех файлов
    a = xlrd.open_workbook('E:\code\Cvi\Cvi\\' + files[i], on_demand=True)

# функция печати названия файла и доставания и печати данных из файлов (из нужных столбцов и строк, они указаны в row[5:41] и rownum

    sheet = a.sheet_by_index(0) # назначения листа из файла
    print (files[i]) # печать названия файла
    for rownum in range(sheet.nrows): # печать данных из файла
        row = sheet.row_values(rownum)
        if rownum > 6:
            print (row[5:41])

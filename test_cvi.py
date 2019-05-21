import csv
import os

# перебрать файлы в папке
# directory =os.walk('E:\code\Cvi\cvitest')
# for d in directory:
#     print (d)

# функция сопоставления строк с перебиранием файлов
def falseCvi():
   # открытие нужного файла
   name = 'E:\code\Cvi\cvitest\\' + d[2][y]
   with open(name, "r") as objcsv:
      reader = csv.reader(objcsv, delimiter=';')
      b = 0
      c = 0
      for row in reader:
         FalseTicker = row[1:41]
         c += 1
         if c > 7:
            if row[1] == '':
               break
            else:
               if FalseTicker == ticker:
                  print('Find false in file ' + e + ' in row ' + str(c))
               # функция чтобы чем то занять программу
               else:
                  b += 1




# открытие файла ЦВИ и проверки его построчно (просмотр каждой его строчки во всех файлах)
directory =os.walk('E:\code\Cvi\cvitest')
for d in directory:
   x=0
   y=len(d[2])-1
   while x<len(d[2])-1:
      # открытие проверяемого файла
      e = 'E:\code\Cvi\cvitest\\' + d[2][x]
      print(e)
      with open(e, "r") as objcsv:
         reader = csv.reader(objcsv, delimiter=';')
         c = 0
         for row in reader:
            ticker = row[1:41]
            c += 1
            if c > 7:
               if row[1] == '':
                  break
               else:
                  falseCvi()

      x += 1

print ('ok')
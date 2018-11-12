__author__ = 'Литаровский Сергей'

print('Задание-1 easy')
print()

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os           # запутался. не работает
path = os.getcwd()
print ("Текущая рабочая директория %s" % path)
ans = str(input("Создать 9 директорий? y / n / q : "))
i = 1
if ans == 'y':          # mkdirs()
        dir_path = os.path.join(os.getcwd(), 'dir_')
    try:
        os.mkdir(dir_path)
    except FileExistsError:
        print('Такая директория уже существует')

elif ans == 'n':
    ans2 = str("Удалить созданные 9 директорий? y / n / q : ")
    i = 1
    if ans2 == 'y':
        i = 1
        if i < 9:
            dir_path2 = os.path.join(os.getcwd(), 'dir_{}', (i))
        try:
            os.rmdir(dir_path2)     # removedirs(path)
            i += i
        except FileExistsError:
            print('Такая директория уже существует')
else:
    exit()

print()
print('Задание-2 easy')
print()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
import os
# print(os.listdir(os.path(os.getcwd())))
root_dir = os.getcwd()
os.listdir(root_dir)
# [y for y in os.listdir(root_dir) if os.path.isfile(os.path.join(root_dir, y))]


print()
print('Задание-3 easy')
print()
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import os
import shutil
ddd = os.getcwd()
shutil.copy(ddd)

# NORMAL Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py
"""
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.
"""

import json

# сортировка
def data_sort(json_dic):
    list = []
    
    for i in json_dic.items():
        value = i[1]
        value.append(i[0])
        list.append(value)
    
    list.sort()        
    return list      
    
#чтение из файла
def read_file():
    with open("data.json", "r", encoding = "UTF-8") as data:
        json_dic = {}
        str = data.readline()
        if len(str) > 0:
            json_dic = json.loads(str)
    return json_dic

#запись файла
def write_file(json_dic):
    with open("data.json", "w", encoding = "UTF-8") as data:  
        json.dump(json_dic, data)

# добавление данных
def add_new_data():
    print("На какую дату необходимо добавить заметку (дата в формате дд.мм.гг): ")
    time = input()
    print("Введите заголовок новой заметки: ")
    header = input()
    print("Введите текст заметки: ")
    msg = input()
    list = [time, header, msg]       
    
    json_dic = read_file()
    if len(json_dic) > 0:            
        flag = True
        k = 0
        while flag == True:
            flag = False               
            for i in json_dic.keys():
                j = int(i)                   
                if k == j:
                    k += 1                                                         
                    flag = True
        json_dic[k] = list            
    else:
        json_dic = {0:list}           
    
    write_file(json_dic)
    print("Заметка добавлена")
         
# вывод данных
def data_output():
    json_dic = read_file()
    list = data_sort(json_dic)
    
    for i in list:
        value = i        
        print("\n" + "Дата: " + value[0] + "\n" + "Заголовок: " + value[1] + "\n" + "Текст: " + value[2] + "\n" + "id заметки: " + value[3] + "\n")   
    
# поиск данных
def find_data():
    flag = False
    i = int(input("Введите требуемое действие:" + "\n" + "1 - для поиска по дате;" + "\n" + "2 - для поиска по заголовку;" + "\n" + ": "))
    if i == 1:
        print("Укажите дату в формате дд.мм.гг): ")
        time = input()
        json_dic = read_file()
        for i in json_dic.items():
            value = i[1]
            if value[0] == time:
                print("\n" + "Дата: " + value[0] + "\n" + "Заголовок: " + value[1] + "\n" + "Текст: " + value[2] + "\n" + "id заметки: " + i[0] + "\n")
                flag = True
    elif i == 2:
        print("Укажите заголовок: ")
        header = input()
        json_dic = read_file()
        for i in json_dic.items():
            value = i[1]
            if value[1] == header:
                print("\n" + "Дата: " + value[0] + "\n" + "Заголовок: " + value[1] + "\n" + "Текст: " + value[2] + "\n" + "id заметки: " + i[0] + "\n") 
                flag = True
    else: print("Действие выбрано неверно")
                
    if flag == False:
        print("Заметка не найдена") 
        
    return flag       

# редактировани данных
def change_data():
    flag = find_data()
    if flag == True:
        print("Укажите id заметки для редактирования")
        id = input()
        print("Укажите новый заголовок: ")
        header = input()    
        print("Введите новый текст заметки: ")
        msg = input()
        flag = False
        
        json_dic = read_file()
        for i in json_dic.keys():                
            if i == id:
                list = json_dic[i]
                list[1] = header
                list[2] = msg
                json_dic[i] = list
                print("Заметка c id: " + id + " изменена")
                flag = True
                write_file(json_dic)
        
        if flag == False:
            print("Неверный id")     

# удаление данных
def delete_data():
    flag = find_data()
    if flag == True:     
        print("Укажите id заметки для удаления: ")
        id = input() 
        flag = False       
        json_dic = read_file()
        
        for i in json_dic.keys():
           if i == id:  
                flag = True
    
    if flag == False:
            print("Неверный id")
    else:
        json_dic.pop(id)
        write_file(json_dic)
        print("Заметка c id: " + id + " удалена")
     

#основная программа
print("Вас приветствует приложение Заметки")
i = 0
while i != 6:
    i = 0
    i = int(input("Введите требуемое действие:" + "\n" + "1 - для добавления записей;" + "\n" + 
                "2 - для поиска записей;" + "\n" + "3 - для изменения записей; " + "\n" + 
                "4 - для удаления записей:" + "\n" + "5 - вывести все записи" + "\n" + 
                "6 - для выхода" + "\n" + ": "))

    if i == 1: add_new_data()
    elif i == 2: find_data()
    elif i == 3: change_data()
    elif i == 4: delete_data()
    elif i == 5: data_output()
    
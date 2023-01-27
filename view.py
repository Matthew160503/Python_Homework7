def select_operation():
    operation = int(input('1 - Добавить пользователя\n2 - Вывести данные файла\n'+
    '3 - вывести имя и фамилию\n4 - Сортировка по имени\n5 - Сортировка по id\n'))
    return operation

def init_information():
    id = int(input('Введите id: '))
    name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    phone_number = int(input('Введите номер телефона: '))
    result = f'{id} {name} {second_name} {phone_number}\n'
    with open("spravocnik.txt","a") as text:
        text.write(result)
    print('Информация успешно сохранена!')
import collections
import datetime

pets = dict()
pet_id = 0


def create(pets, pet_id):
    last = collections.deque(pets, maxlen=1)
    pets_name = dict()
    name = input("Введите имя питомца: ")
    pets_type = input("Введите тип питомца ")
    pets_age = int(input("Введите возраст питомца: "))
    pets_owner = input("Введите имя хозяина питомца: ")
    pets_name[name] = {"Pet's type": pets_type,
                       "Pet's age": pets_age,
                       "Pet's owner": pets_owner}
    if len(pets) != 0:  # Проверка на наличие этого питомца в словаре
        id_in_base = list(pets.keys())
        for i in id_in_base:
            check_base = pets[i]
            if check_base == pets_name:
                print("Такой питомец, уже записан. Попробуйте снова")
                return (pet_id)
    pet_id += 1
    pets[pet_id] = pets_name
    return (pet_id)


def read(pets):
    pet_id = int(input("Введите идентификационный номер питомца: "))
    pets_information = get_pet(pets, pet_id)
    if pets_information == False:
        print("Ошибка. Такой идентификационный номер отсутствует в базе")
        return None
    name = list(pets_information)
    name = name[0]
    information = list(pets_information.values())
    type = (information[0]["Pet's type"])
    age = (information[0]["Pet's age"])
    years = get_suffix(information)
    owner = (information[0]["Pet's owner"])
    inf_of_pets = str(
        f'Это {type} по кличке "{name}". Возраст питомца: {age} {years}. Имя владельца: {owner}')
    print(inf_of_pets)


def update(pets):
    pet_id = int(input("Введите идентификационный номер питомца: "))
    pets_information = get_pet(pets, pet_id)
    pets_name = dict()
    name = input("Введите имя питомца: ")
    pets_type = input("Введите тип питомца ")
    pets_age = int(input("Введите возраст питомца: "))
    pets_owner = input("Введите имя хозяина питомца: ")
    pets_name[name] = {"Pet's type": pets_type,
                       "Pet's age": pets_age,
                       "Pet's owner": pets_owner}
    pets[pet_id] = pets_name


def delete_from_pets(pets):
    pet_id = int(
        input("Введите идентификатор питомца, которого необходимо удалить "))
    if pet_id not in pets.keys():
        print(
            "Ошибка. Такой идентификатор питомца отсутствует. Удаление невозможно.")
    else:
        del pets[pet_id]


def get_pet(pets, pet_id):
    if pet_id not in pets.keys():
        print("Ошибка. Такой идентификационный номер отсутствует в базе")
        return False
    pets_information = pets[pet_id]
    return pets_information


def get_suffix(information):
    string = ""
    age = int(information[0]["Pet's age"])
    if (age == 1):
        string = "год"
    elif (age > 20) and (age % 10) == 1:
        string = "год"
    elif (age > 0) and (age < 5):
        string = "года"
    elif (age > 20) and ((age % 10) > 0) and ((age % 10) < 5):
        string = "года"
    else:
        string = "лет"
    return string


def pets_list(pets):
    id_in_base = list(pets.keys())
    print("Записи содержащиеся в базе: ")
    for i in id_in_base:
        print(i, pets[i])


command = ''
while command != 'stop':
    print("Выберите и введите одну из нижеследующих команд:")
    print("create - \t создать запись в базу данных")
    print("read -  \t прочитать запись о питомце из базы данных")
    print("update - \t обновить информацию о питомце в базе данных")
    print("delete - \t удалить информацию о питомце из базы данных")
    print("stop -  \t остановить выполнение программы")
    command = input()
    if command == 'create':
        pet_id = create(pets, pet_id)
    elif command == 'read':
        read(pets)
    elif command == 'update':
        update(pets)
    elif command == "delete":
        delete_from_pets(pets)
    elif command == "stop":
        continue
    else:
        print("Ошибка. Введена неправильная команда. Попробуйте еще раз")
pets_list(pets)

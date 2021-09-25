# Очистка  директории по таймеру

import os, schedule, time


def show_current_dir():
    # Возвращает текущую директорию
    current_dir = str(os.getcwd())
    return current_dir


def input_path_to_dir():
    # Получет от пользователя путь к директории и возвращает её
    user_path = input(str('Введите путь к директории, из которой нужно удалить все файлы '
                          '\n(пример: C:\Program Files\\test) и нажмите ENTER: '))
    return user_path


def change_dir(atr):
    # Изменияет директорию на пользовательскую
    user_path = atr
    os.chdir(user_path)


def list_dir(atr):
    # Принимает директорию пользователя и возвращает список файлов в указанной директории
    user_current_dir = atr
    user_current_list_dir = os.listdir(user_current_dir)
    return user_current_list_dir


def remove_files(atr):
    # Удаляем файлы из указанной пользователем директории. Передаем функции список файлов из директории
    user_list_dir = atr
    try:
        for file in user_list_dir:
            # Проверяем каждый элемент списка, файл он или нет. Если файл - удаляем,
            # если не файл (директория или ссылка) - не удаляем.
            if os.path.isfile(file):
                os.remove(file)
            else:
                print(f'[{file}] - Не удалено (это не файл)')
    except PermissionError:
        print("Ошибка удаления (отказано в доступе).\nДля удаления системных файлов или файлов из системной "
              "директории - перезапустите программу с правами администратора.")


def for_schedule(arg):
    # Функция для таймера (библиотека schedule).
    # Получаем список всех папок и файлов пользовательской директории
    user_path = arg
    user_list_dir = list_dir(user_path)

    # Удаляем все файлы из указанного списка:
    remove_files(user_list_dir)

    # Получаем содержимое директории после удаления файлов
    user_list_dir = list_dir(user_path)
    print(f'Директория после удаления файлов:\n{user_list_dir}')


def choice_time():
    # Пользователь выбирает день и время для еженедельного запуска расписания
    print("Создание расписания:")
    user_day_choice = int(input("Введите день недели цифрой: "))
    user_time_choice = input("Введите время в формате ЧЧ:ММ: ")
    if user_day_choice == 1:
        schedule.every().monday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 2:
        schedule.every().tuesday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 3:
        schedule.every().wednesday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 4:
        schedule.every().thursday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 5:
        schedule.every().friday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 6:
        schedule.every().saturday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    if user_day_choice == 7:
        schedule.every().sunday.at(f"{user_time_choice}").do(for_schedule, arg=user_path)
    print('--------------------------------------------------------------------------')

# Показываем текущую директорию
current_dir = show_current_dir()
print(f'Текущая директория: {current_dir}')
print('--------------------------------------------------------------------------')

# Показываем измененную пользователем диреткорию
user_path = input_path_to_dir()
print('--------------------------------------------------------------------------')
print(f'Вы указали путь: {user_path}')
print('--------------------------------------------------------------------------')

# Изменяем текущую директорию на введенную пользователем (передаем параметр - путь пользователя)
change_dir(user_path)

# запускаем функцию выбора таймера
choice_time()


while True:
    schedule.run_pending()
    time.sleep(1)

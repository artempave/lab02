from Clients.ClientRecvAllCur import ClientRecvAllCurr
from Clients.ClientRecvTranslateCur import ClientRecvTranslate
from Struct.Users import User
from Library.LibResurse import LibResurce
from Struct.Bank import Bank

class Terminal:
    def __init__(self):
        self.commands = {
            "-help": self.show_help,
            "-exit": self.exit_terminal,
            "-showc": self.show_cur,
            "-exch": self.get_exchange,
            "-tran": self.trans_cur,
            "-crtu": self.create_user,
            "-showu": self.show_users,
            "-tranm": self.transfer_money,
            "-checkb": self.check_balance
        }
        self.all_users = {}
        self.all_banks = {}
        LibResurce().load_all_banks(self.all_banks)
        LibResurce().load_all_users(self.all_users, self.all_banks)


    def start(self):
        print("Добро пожаловать в терминал! Введите '-help' для получения списка команд.")
        while True:
            command = input("> ")
            self.execute_command(command)

    def execute_command(self, command):
        command = command.strip().lower()
        if command in self.commands:
            self.commands[command]()
        else:
            print(f"Неизвестная команда: {command}. Введите '-help' для получения списка доступных команд.")

    def show_help(self):
        print("Доступные команды:")
        print("  -help - показать список доступных команд")
        print("  -exit - выйти из терминала")
        print("  -showc - вывести все ID валют")
        print("  -exch - вернуть курс валюты относительно другой")
        print("  -tran - перевести из одной валюты в другую")
        print("  -crtu - создать новый банковский счет")
        print("  -showu - показать всех пользователей")
        print("  -tranm - перевод денег от одного пользователя к другому")
        print("  -checkb - проверка баланса")

    def exit_terminal(self):
        print("Выход из терминала. Всего доброго!")
        exit()
    def show_cur(self):
        print("Список всех ID валют:")
        ClientRecvAllCurr().print_all_currency()

    def get_exchange(self):
        print("Курс:")
        cur_1 = input("  ID первой валюты >> ").strip().upper()
        cur_2 = input("  ID второй валюты >> ").strip().upper()

        _ClientRecvTranslate = ClientRecvTranslate()
        _ClientRecvTranslate.exchange_currency(cur_1, cur_2, "1", )
        _ClientRecvTranslate.exchange_currency(cur_2, cur_1, "1", )

    def trans_cur(self):
        print("Перевод одной валюты в другую:")
        cur_1 = input("  ID первой валюты >> ").strip().upper()
        cur_2 = input("  ID второй валюты >> ").strip().upper()
        amount = input("  размер перевода  >> ").strip()

        _ClientRecvTranslate = ClientRecvTranslate()
        _ClientRecvTranslate.exchange_currency(cur_1, cur_2, amount, )

    def create_user(self):
        print("Создания нового счета:")
        mail = input("  введите вашу почту  >> ").strip()
        if mail in self.all_users:
            print(f"Ошибка: пользователь с '{mail}' уже существует.")
        else:
            password = input("  введите ваш пароль  >> ").strip()
            name = input("  введите ваше имя    >> ").strip()
            country = input("  введите вашу страну >> ").strip()
            print("Теперь выбирите свой банк:")
            for bank in self.all_banks:
                self.all_banks[bank].display_info()
            bank = input("  введите ID банка    >> ").strip()
            if int(bank) in self.all_banks:
                print("Теперь выбирите валюту:")
                flag = ClientRecvAllCurr().print_all_currency()
                if flag == 0:
                    curr = input("  введите ID валюты   >> ").strip().upper()
                    self.all_users[mail] = User(mail, password, name, country, self.all_banks[int(bank)], curr, 1000)
                    LibResurce().save_new_user(self.all_users[mail])
                    print("Вы успешно зарегистрировали нового пользователя")
            else:
                print(f"Ошибка: неизвестный ID банка '{bank}'.")

    def show_users(self):
        print("Список всех пользлвателей")
        for user in self.all_users:
            print(self.all_users[user].get_inf())

    def transfer_money(self):
        print("Начинаем транзакцию")
        mail = input("  введите вашу почту      >> ").strip()
        if mail in self.all_users:
            password = input("  введите ваш пароль      >> ").strip()
            if password == self.all_users[mail].get_pass():
                print(self.all_users[mail].get_balance())
                user = input("  введите почту получателя >> ").strip()
                if user in self.all_users:
                    count = input("  введите сумму перевода   >> ").strip()
                    self.all_users[mail].transfer_money(float(count), self.all_users[user])
                else:
                    print(f"Ошибка: пользователь с '{user}' не найден.")
            else:
                print(f"Ошибка: пароль неверный.")
        else:
            print(f"Ошибка: пользователь с '{mail}' не найден.")

    def check_balance(self):
        print("Проверка баланса:")
        mail = input("  введите вашу почту      >> ").strip()
        if mail in self.all_users:
            password = input("  введите ваш пароль      >> ").strip()
            if password == self.all_users[mail].get_pass():
                print(self.all_users[mail].get_balance())
            else:
                print(f"Ошибка: пароль неверный.")
        else:
            print(f"Ошибка: пользователь с '{mail}' не найден.")









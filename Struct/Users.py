from Struct.Currency import Currency
from Struct.Bank import Bank

class User:

    def __init__(self, mail: str, password: str, name: str, country: str, bank: Bank, code: str, count: float):
        self.mail = mail
        self.name = name
        self.password = password
        self.country = country
        self.bank = bank
        self.Currency = Currency(code, count)

    def get_currency(self):
        return self.Currency

    def get_mail(self):
        return f"{self.mail}"

    def get_pass(self):
        return self.password

    def get_name(self):
        return f"{self.name}"

    def get_balance(self):
        return f"Ваш баланс: {self.Currency.get_count()} {self.Currency.get_code()}"

    def get_location(self):
        return f"{self.mail} живет в {self.country}"

    def get_inf(self):
        return f"почта {self.mail} живет в {self.country} использует банк {self.bank.get_name()}"

    def transfer_money(self, count_tr, user_2):
        if self.Currency.count - count_tr < 0:
            print("Ошибка: недостаточно средств")
            return

        com = self.bank.calculate_commission(count_tr)
        if (user_2.get_currency() + Currency(self.Currency.get_code(), count_tr - com)) == 0:
            self.Currency.def_count(count_tr)
            print(f"Коммисия вычтена {com} {self.Currency.get_code()}, переведено {count_tr - com} {self.Currency.get_code()}")
            print(f"Транзакция завершилась успехом. {self.get_balance()}")

    def __str__(self):
        return f"{self.mail} {self.password} {self.name} {self.country} {self.bank.get_id()} {self.Currency}"

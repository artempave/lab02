class Bank:
    BANK_TVER_ID = 1
    BANK_ALFA_ID = 2
    BANK_BEZ_OBMANA_ID = 3

    def __init__(self, bank_id, name, commission_rate):
        self.bank_id = bank_id
        self.name = name
        self.commission_rate = commission_rate

    def get_id(self):
        return f"{self.bank_id}"
    def get_name(self):
        return f"{self.name}"

    def display_info(self):
        print(f"ID банка: {self.bank_id}")
        print(f"Название банка: {self.name}")
        print(f"Процент комиссии: {self.commission_rate}%")

    def calculate_commission(self, amount):
        commission = amount * (self.commission_rate / 100)
        return commission


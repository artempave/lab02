from Struct.Users import User
from Struct.Bank import Bank

class LibResurce:
    USERS_RES = "users.txt"

    def load_all_users(self, all_users, all_bank):
        with open(self.USERS_RES, "r") as file:
            lines = file.readlines()
            for line in lines:
                list_line = line.strip().split()
                all_users[list_line[0]] = User(list_line[0], list_line[1], list_line[2], list_line[3], all_bank[int(list_line[4])], list_line[5], float(list_line[6]))
                #print(all_users[list_line[0]])

    def save_new_user(self, info):
        with open(self.USERS_RES, "a") as file:
            file.write(f"{info}\n")

    def load_all_banks(self, all_banks):
        all_banks[Bank.BANK_TVER_ID] = Bank(Bank.BANK_TVER_ID, "TverBank", 2.5)
        all_banks[Bank.BANK_BEZ_OBMANA_ID] = Bank(Bank.BANK_BEZ_OBMANA_ID, "ObmanyNetBank", 60)
        all_banks[Bank.BANK_ALFA_ID] = Bank(Bank.BANK_ALFA_ID, "AlfaBank", 5)


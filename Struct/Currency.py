from Clients.ClientRecvTranslateCur import ClientRecvTranslate


class Currency:
    def __init__(self, code: str, count: float):
        self.code = code
        self.count = count
    def get_code(self):
        return self.code
    def get_count(self):
        return self.count

    def def_count(self, n_count):
        self.count -= n_count

    def __add__(self, other):
        if self.code != other.get_code():
            _ClientRecvTranslate = ClientRecvTranslate()
            new_amount = []
            flag = _ClientRecvTranslate.exchange_currency(other.get_code(), self.code, str(other.get_count()), new_amount)
            #print(new_amount[0])
            if flag == 0:
                self.count += new_amount[0]
            return flag
        else:
            self.count += other.get_count()
        return 0

    def __str__(self):
        return f"{self.code} {self.count}"


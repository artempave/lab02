import socket
from Library.LibServerConnection import LibServerConnection


class ClientRecvTranslate(LibServerConnection):
    def exchange_currency(self, first_currency, second_currency, amount_currency, res_curr=None):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.SERVER_HOST, self.SERVER_PORT))

            flag_check_db = self.recv(sock, 1)
            if int(flag_check_db) == LibServerConnection.ERROR_DB_CONNECTION:
                sock.close()
                return self.ERROR_DB_CONNECTION

            self.send(sock, '1', 1)
            self.send(sock, first_currency)
            self.send(sock, second_currency)
            self.send(sock, amount_currency)

            flag_check_sql_request = self.recv(sock, 1)
            flag_int_sql_request = int(flag_check_sql_request)

            if flag_int_sql_request == self.ERROR_DB_REQUEST:
                sock.close()
                print("Ошибка: Не удалось выполнить запрос к базе данных")
                return self.ERROR_DB_REQUEST
            elif flag_int_sql_request == self.ERROR_SYNTAX:
                sock.close()
                print("Ошибка: Не верный синтаксис данных")
                return self.ERROR_SYNTAX
            elif flag_int_sql_request == self.ERROR_CURRENCY:
                sock.close()
                print("Ошибка: валюта не найдена")
                return self.ERROR_CURRENCY

            new_amount_currency = self.recv(sock)
            data_time = self.recv(sock, 13)
            sock.close()
            data_time_split = data_time.split()

            #print(f"Дата и время последнего изменения: {data_time}")
            print(f"{amount_currency} {first_currency} = {new_amount_currency} {second_currency} на {data_time_split[0]}.{data_time_split[1]}.{data_time_split[2]} {data_time_split[3]}:00")
            if res_curr != None:
                res_curr.append(float(new_amount_currency))
            #print("Успешное завершение")
            return 0

        except Exception as e:
            print(f"{self.ERROR_TAG} Ошибка подключения: {e}")
            return self.ERROR_SERVER_CONNECTION

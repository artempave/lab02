import socket
from Library.LibServerConnection import LibServerConnection


class ClientRecvAllCurr(LibServerConnection):
    def print_all_currency(self):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((self.SERVER_HOST, self.SERVER_PORT))
            flag_check_db = self.recv(sock, 1)
            if int(flag_check_db) == self.ERROR_DB_CONNECTION:
                sock.close()
                print("Ошибка: не удалось подключиться к базе данных")
                return self.ERROR_DB_CONNECTION

            self.send(sock, "9", 1)
            flag_check_sql_request = self.recv(sock, 1)
            flag_int_sql_request = int(flag_check_sql_request)

            if flag_int_sql_request == self.ERROR_DB_REQUEST:
                sock.close()
                print("Ошибка: не удалось выполнить запрос к базе данных")
                return self.ERROR_DB_REQUEST

            cols = self.recv(sock)
            int_cols = int(cols)

            kol = 0
            result_str = ""
            for i in range(int_cols):
                currency_name = self.recv(sock)
                result_str += f" {currency_name}"
                kol+=1
                if kol == 16 or i == int_cols-1:
                    print(result_str)
                    kol = 0
                    result_str = ""
            #print("Успешное завершение")
            sock.close()
            return self.CORRECT_PERF

        except Exception as e:
            print(f"{self.ERROR_TAG} Ошибка подключения: {e}")
            return LibServerConnection.ERROR_SERVER_CONNECTION

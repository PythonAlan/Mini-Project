import json
import socket
Host = '127.0.0.1'
Port = 53001
error_time = 3;
list = [{"name": 'a', "pwd": '123'}, {"name": 'b', "pwd": '456'}]
error_report = open('report.txt',"w+")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#默认建立tcp链接
s.bind((Host,Port))#绑定ip和接口
s.listen(1)
while True:
    conn,addr=s.accept()
    data = conn.recv(1024)
    if data:
        print(addr)
        conn.send(bytes('fsfs',encoding="utf-8"))
























# while True:
#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind((Host, Port))
#     s.listen(1)
# error_time = 3;
# list = [{"name": 'a', "pwd": '123'}, {"name": 'b', "pwd": '456'}]
#
# for dict in list:
#     if dict["name"] == name and dict["pwd"] == passwd:
#         print("Welcom to system")
#     else:
#         print("Validation false")






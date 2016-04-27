import socket
import json

Host = '127.0.0.1'
Port = 53002
error_time = 3
list = [{"name": 'a', "pwd": '123'}, {"name": 'b', "pwd": '456'}]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 默认建立tcp链接
s.bind((Host, Port))  # 绑定ip和接口
s.listen(1)
while True:
    error_report = open('report.txt', "r")
    content = error_report.read()
    error_report.close()
    if content == '':
        d = {}
    else:
        d = eval(content)
    conn, addr = s.accept()
    data = conn.recv(1024)

    if data:
        ip_name = addr[0]
        data = bytes.decode(data)
        userinfo = data.split(",")
        if ip_name in d.keys():#判断字典key是否存在
            if (int(d[ip_name]) >= 5):
                conn.send(bytes('5', encoding="utf-8"))
            else:
                for dict in list:
                    if dict['name'] == userinfo[0] and dict['pwd'] == userinfo[1]:
                        conn.send(bytes('0', encoding="utf-8"))
                        break
                    else:
                        error_report2 = open('report.txt', "w")
                        d[ip_name] = int(d[ip_name]) + 1

                        new_content = json.dumps(d)
                        error_report2.write(new_content)
                        error_report2.close()
                        conn.send(bytes(str(d[ip_name]), encoding="utf-8"))
                        break
        else:
            for dict in list:
                if dict['name'] == userinfo[0] and dict['pwd'] == userinfo[1]:
                    conn.send(bytes('0', encoding="utf-8"))
                    break
                else:
                    error_report2 = open('report.txt', "w")
                    d[ip_name] = 1
                    new_content = json.dumps(d)

                    error_report2.write(new_content)
                    error_report2.close()
                    conn.send(bytes('1', encoding="utf-8"))
                    break


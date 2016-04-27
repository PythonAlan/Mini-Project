import socket  # 导入socket
import sys

Host = '127.0.0.1'
Port = 53002

def sendSocket(host=Host, port=Port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 建立socket链接
    s.connect((Host, Port))  # 客户端链接服务端
    name = input("input your name:")
    passwd = input("input your passwd:")
    data = bytes('%s,%s' % (name, passwd), encoding="utf-8")
    s.send(data)
    flag = True
    while flag==True:
        result = s.recv(1024)  # 接收打印
        result_num = bytes.decode(result)   #字节转换
        if result_num == '0':
            print("welcom")
            s.close()
            sys.exit()
        elif result_num == '5':
            print("this IP is locked")
            s.close()
            sys.exit()
        else:
            print("try again")
            sendSocket(host=Host, port=Port) #递归

sendSocket()

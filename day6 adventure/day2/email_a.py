#!/usr/bin/env python3

#antuor:Alan



import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import time, os

# to_add = input('请输入收件邮箱:')
# msg = MIMEText('喂,我啊', 'plain', 'utf-8')       #邮件内容可以加载文件
# msg['From'] = formataddr(["吕毅",'37172515@qq.com'])
# msg['To'] = to_add
# msg['Subject'] = "自动化测试"
#
# server = smtplib.SMTP_SSL('smtp.qq.com',465)
# server.connect('smtp.qq.com',465)
# server.login("371725153@qq.com", "python")
# server.sendmail('371725153@qq.com', [to_add], msg.as_string())
# server.quit()


########################################测试成功#######################################
to_mail = input('请输入收件邮箱:')  #收件人
email_text = input('请输入邮件内容:')  #邮件内容

def send_mail(from_mail='371725153@qq.com'):


    msg = MIMEText(email_text,'plain','utf-8')  #文本内容
    msg['Subject'] = email_text         #主题
    msg['from'] = from_mail             #收件人


    mail = smtplib.SMTP_SSL('smtp.qq.com',465)
    mail.connect('smtp.qq.com',465)
    mail.login('371725153@qq.com','python')
    mail.sendmail(from_mail,to_mail,msg.as_string())
    mail.close()
    print ('发送邮件成功')

try:
    flag = False
    i = 0
    while True:
        send_mail(from_mail='371725153@qq.com')
        time.sleep(60)
        i +=1
        if i >10:
            flag = True
            break

        else:
            continue

except RuntimeError:
    print ("smtplib.SMTPServerDisconnected: Connection unexpectedly closed")


else :
    print("没任何异常,程序结束")



# if __name__ == "__main__":
#     send_mail(to_mail,email_text,from_mail='371725153@qq.com')














import smtplib
import sys
from email.mime.text import MIMEText


def sendMail(to, content):
    mail_host = 'smtp.163.com'  
    mail_user = '18810687830@163.com'  
    mail_pass = 'sb18810687830sb'   
    sender = '18810687830@163.com'  
    receivers = to

    message = MIMEText(content,'plain','utf-8')
    message['Subject'] = 'Buy Key From Smart Signature' 
    message['From'] = sender 
  
    message['To'] = to

    #登录并发送邮件
    try:
        smtpObj = smtplib.SMTP() 
        #连接到服务器
        smtpObj.connect(mail_host,25)
        #登录到服务器
        smtpObj.login(mail_user,mail_pass) 
        #发送
        smtpObj.sendmail(
            sender,receivers,message.as_string()) 
        #退出
        smtpObj.quit() 
        print('success')
    except smtplib.SMTPException as e:
        print('error',e) #打印错误

def main():
    if len(sys.argv) != 3:
        print("Error: invalid parameters")
    else:
        print('发送Key %s 致 %s 邮箱：' % (sys.argv[1],sys.argv[2])
        sendMail(argv[1], argv[2])

if __name__ == "__main__":
    main()

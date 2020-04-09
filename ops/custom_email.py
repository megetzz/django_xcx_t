import os
import django
import smtplib
from helloword import settings

from email.mime.text import MIMEText


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myfirstproj.settings')
django.setup()


def send_mail():
    # 实例个 mimetext 对象
    msg = MIMEText("邮件通道测试,马宇超", "plain", "utf-8")
    # 发件人
    # msg['FROM'] = "Mail Test"
    msg['FROM'] = "ma.1971250916@qq.com"
    # 主题
    msg['Subject'] = "【Mail Test】"
    # 接收者
    receivers = ['ma.1971250916@qq.com','myc766686879@qq.com']
    # 服务器
    # 加密的服务器
    # server = smtplib.SMTP_SSL(settings.EMAIL_HOST, settings.EMAIL_PORT)
    # 不带加密的服务器/
    server = smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT)
    server.set_debuglevel(1)
    server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
    server.sendmail(settings.EMAIL_FROM, receivers, msg.as_string())
    server.close()
    pass


if __name__ == '__main__':
    send_mail()
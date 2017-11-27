# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
import os.path

mail_host = ''
mail_port = 587
mail_user = ''
mail_pass = ''
sender = ''
receivers = ['']


def send_email(subject, content, attach_image_path=None):
    # 设置email信息
    # 邮件内容设置
    message = MIMEMultipart('related')
    text_content = MIMEText(content, 'plain', 'utf-8')
    message.attach(text_content)
    # 邮件主题
    message['Subject'] = subject
    # 非空条件下，构造图片附件
    if attach_image_path is not None:
        att = MIMEImage(open(attach_image_path, 'rb').read())
        att.add_header('Content-ID', os.path.basename(attach_image_path))
        message.attach(att)

    # 发送方信息
    message['From'] = sender
    # 接受方信息
    message['To'] = receivers[0]

    # 登录并发送邮件
    try:
        smtpObj = smtplib.SMTP()
        # 连接到服务器
        smtpObj.connect(mail_host, mail_port)
        smtpObj.starttls()
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
    except Exception, e:
        print e


if __name__ == '__main__':
    send_email('test', 'test')
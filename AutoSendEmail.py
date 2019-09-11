#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 使用python发送邮件，需要授权码，它是用于登录第三方邮件客户端的专用密码
 
import smtplib
import os
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from email.mime.base import MIMEBase
from email import encoders
 
# 第三方 SMTP 服务
mail_host="smtp.qq.com"  #设置服务器
mail_user="2509552914@qq.com"    #邮箱用户名
mail_pass="kfhzletcekegdjfi"   #授权码
scheme = 'Unity-iPhone'
#时间字符串
time_Tag = '%s'%(time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time())))
 
sender = '2509552914@qq.com'
receivers = ['2509552914@qq.com']  # 接收邮件，多个收件人用逗号隔开

message = MIMEMultipart()

#构造纯文本邮件内容
message.attach(MIMEText('【%s】'%scheme + 'iOS 测试项目完成，请下载测试！如有问题，请联系iOS相关人员，我们会及时解决，谢谢!', 'plain', 'utf-8'))#发邮件内容
message['From'] = Header('自动打包系统<%s>' % sender, 'utf-8') # 发件人
message['To'] =  Header("测试人员", 'utf-8') #收件人
message['Subject'] = Header('【%s】'%scheme + 'iOS客户端测试包构建完成, 构建时间:%s'%(time_Tag), 'utf-8').encode() #邮件主题

# 构造附件，传送当前目录下的 avatar.png 文件
# 添加图片类型附件
local_path_filename = os.path.expanduser('/Users/yostar/Desktop/日常工作/工程/准备/撕衣服/Beauty/g2_up.png')
if(os.path.exists(local_path_filename)):
    with open(local_path_filename, 'rb') as imageFile:
        mime = MIMEBase('image', 'png', filename = 'g2_up.png')
        mime.add_header('Content-Disposition', 'attachment', filename='g2_up.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(imageFile.read())
        encoders.encode_base64(mime)
        message.attach(mime)

try:
    smtpObj = smtplib.SMTP() 
    smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
#    ss = smtplib.SMTP_SSL("smtp.qq.com", 465) #这个方法的端口号是465
    smtpObj.login(mail_user,mail_pass)  
    smtpObj.sendmail(sender, receivers, message.as_string())# 参数分别是发送者，接收者，第三个是把上面的发送邮件的内容变成字符串
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
finally:
    smtpObj.quit() # 发送完毕后退出smtp

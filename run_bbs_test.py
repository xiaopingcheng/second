from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

# 定义发送邮件
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['From'] = '17727820013@163.com'
    msg['To'] = "820961283@qq.com"
    msg['Subject'] = Header('自动化测试报告', 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.163.com')
    smtp.login('17727820013@163.com', 'abc1234')# 填写授权码
    # try :
    #     smtp.sendmail('13487877976@163.com', '17727820013@163.com', msg.as_string())
    #     print('email has send out !')
    # except:
    #     print('发送失败')

    smtp.sendmail('17727820013@163.com', '820961283@qq.com', msg.as_string())
    smtp.quit()
    print('email has send out !')


# ==查找测试报告目录，找到最新生成的测试报告文件==
def new_report(filepath):
    lists = os.listdir(filepath) # 返回包含文件名字的目录列表，
    lists.sort(key = lambda fn: os.path.getmtime(filepath + fn))# 返回文件最新更改时间,fn参数就是lists中的元素
    file_new = os.path.join(filepath, lists[-1])
    return  file_new

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    filename = './子项目bbs社区/report/HTMLreport/' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='163邮箱登录自动化测试报告',
                            description='环境：win7 浏览器：Chrome')
    discover = unittest.defaultTestLoader.discover('./子项目bbs社区/test_case/',
                                                       pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    newestReport = new_report('./子项目bbs社区/report/HTMLreport/') # 查找新生成的报告，一个点表示从当前目录开始
    send_mail(newestReport)

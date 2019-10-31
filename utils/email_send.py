from random import Random
from django.core.mail import send_mail
import yagmail
from users.models import EmailVerifyRecord
from django_auth_example.settings import EMAIL_FROM

# 生成随机字符串
def random_str(random_length=8):
    str = ''
    # 生成字符串的可选字符串
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str
# 发送注册邮件
def random_code(random_length=6):
    str = ''
    # 生成字符串的可选字符串
    chars = '1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0, length)]
    return str

def send_register_email(email, send_type="register"):
    # 发送之前先保存到数据库，到时候查询链接是否存在
    # 实例化一个EmailVerifyRecord对象
    email_record = EmailVerifyRecord()
    # 生成随机的code放入链接
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    # 定义邮件内容:
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "教育卫星注册激活链接"
        email_body = "请点击下面的链接激活你的账号: https://education-satellite-morehappysoftware.app.secoder.net/active/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，发件人邮箱地址，收件人（是一个字符串列表）
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        # 如果发送成功
        # if send_status:
        #     print('send_email success!')
        # else:
        #     print('send_email failed~')

def yag_send_register_email(email, send_type="register"):
    # 生成随机的code放入链接
    # 定义邮件内容:
    if send_type == "register":
        code = random_str(16)
        email_title = "航天创客注册激活链接"
        email_body = "请点击下面的链接激活你的账号: https://education-satellite-morehappysoftware.app.secoder.net/active/{0}".format(code)
    elif send_type == "update_email":
        code = random_code(6)
        email_title = "航天创客用户邮箱修改"
        email_body  = "你的验证码为{0}，该验证码用于修改您的个人邮箱，若非本人操作请忽略".format(code)
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    sender = '1308478462@qq.com'
    passwd = 'ztebpgredppmggee'
    yag = yagmail.SMTP(user=sender, password=passwd, host='smtp.qq.com', smtp_ssl=True)
    status = yag.send(to=email, subject=email_title, contents=email_body)
    return status

if __name__ == '__main__':
    status = yag_send_register_email('906866139@qq.com')
    if not status:
        print(status)



from django.test import TestCase
from users.models import User,EmailVerifyRecord,MobileVerify
# Create your tests here.
from django.test import TestCase
from video.models import Video

class UsersModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        User.objects.create(nickname='alice')
        EmailVerifyRecord.objects.create(code='123456')
        MobileVerify.objects.create(code='123456')

    def test_is_admin_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('is_admin').verbose_name
        self.assertEquals(field_label,'管理员')
        
    def test_nickname_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('nickname').verbose_name
        self.assertEquals(field_label,'nickname')

    def test_mobile_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('mobile').verbose_name
        self.assertEquals(field_label,'电话')

    def test_birthday_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('birthday').verbose_name
        self.assertEquals(field_label,'生日')

    def test_gender_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('gender').verbose_name
        self.assertEquals(field_label,'性别')
    
    def test_address_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('address').verbose_name
        self.assertEquals(field_label,'地址')


    def test_image_label(self):
        name=User.objects.get(id=1)
        field_label=name._meta.get_field('image').verbose_name
        self.assertEquals(field_label,'image')

    def test_code_label(self):
        name=EmailVerifyRecord.objects.get(id=1)
        field_label=name._meta.get_field('code').verbose_name
        self.assertEquals(field_label,'验证码')

    def test_email_type_label(self):
        name=EmailVerifyRecord.objects.get(id=1)
        field_label=name._meta.get_field('email').verbose_name
        self.assertEquals(field_label,'邮箱')

    def test_send_type_label(self):
        name=EmailVerifyRecord.objects.get(id=1)
        field_label=name._meta.get_field('send_type').verbose_name
        self.assertEquals(field_label,'send type')


    def test_send_time_label(self):
        name=EmailVerifyRecord.objects.get(id=1)
        field_label=name._meta.get_field('send_time').verbose_name
        self.assertEquals(field_label,'send time')

    def test_mobile_code_label(self):
        name=MobileVerify.objects.get(id=1)
        field_label=name._meta.get_field('code').verbose_name
        self.assertEquals(field_label,'验证码')

    def test_send_mobile_label(self):
        name=MobileVerify.objects.get(id=1)
        field_label=name._meta.get_field('mobile').verbose_name
        self.assertEquals(field_label,'电话')

    def test_send_mobile_time_label(self):
        name=MobileVerify.objects.get(id=1)
        field_label=name._meta.get_field('send_time').verbose_name
        self.assertEquals(field_label,'send time')




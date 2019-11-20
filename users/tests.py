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

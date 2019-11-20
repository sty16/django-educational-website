from django.test import TestCase
from video.models import Video

class VideoModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Video.objects.create(title='alice',description="alice's video")

    def test_title_label(self):
        name=Video.objects.get(id=1)
        field_label=name._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')
        
    def test_description_label(self):
        name=Video.objects.get(id=1)
        field_label=name._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_file_label(self):
        name=Video.objects.get(id=1)
        field_label=name._meta.get_field('file').verbose_name
        self.assertEquals(field_label,'file')

    def test_create_time_label(self):
        name=Video.objects.get(id=1)
        field_label=name._meta.get_field('create_time').verbose_name
        self.assertEquals(field_label,'create time')

    def test_title_max_length(self):
        name=Video.objects.get(id=1)
        max_length=name._meta.get_field('title').max_length
        self.assertEquals(max_length,100)



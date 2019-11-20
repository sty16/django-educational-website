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


class VideoViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        num_of_videos = 5
        #Set up non-modified objects used by all test methods
        for video_num in range(num_of_videos):
            Video.objects.create(title='video %s' % video_num,description="description %s" % video_num)

    def test_video_url(self):
        resp=self.client.get('/video/')
        self.assertEqual(resp.status_code,200)
    
    def test_video_detail_url(self):
        video_num=0
        resp=self.client.get('/video/'+str(video_num+1)+'/')
        self.assertEqual(resp.status_code,200)

    def test_use_correct_template(self):
        resp = self.client.get('/video/')
        self.assertTemplateUsed(resp,'video/index.html')

    def test_use_correct_detail_template(self):
        resp = self.client.get('/video/1/')
        self.assertTemplateUsed(resp,'video/detail.html')

    def test_video_in_context(self):
        resp = self.client.get('/video/')
        self.assertTrue('video_list' in resp.context)
    
    def test_video_detail_in_context(self):
        resp = self.client.get('/video/1/')
        self.assertTrue('video' in resp.context)
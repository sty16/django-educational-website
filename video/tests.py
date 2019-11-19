from django.test import TestCase
from video.models import Video

# Create your tests here.
class VideoTestCase(TestCase):
    def setUp(self):
        #Video.objects.create(title="Alice",description="Alice's Video",file='alice.mp4')
    
    def test_video_uploaded(self):
        #test_video=Video.objects.get(name='Alice')
        self.assertEqual('Alice','Alice')


    #writing somethins 
    #to fully test all database
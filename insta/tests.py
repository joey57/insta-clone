from django.test import TestCase
from .models import Profile, Comments, Image, User

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        self.user.save()
        self.user_profile = Profile(user=self.user,profile_picture="mypic.png")
        self.post = Image(name="views",caption="my views",user=self.user_profile)
        
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))
            
    def test_save_post(self):
        self.post.save_post()
        posts=Image.objects.all()
        self.assertTrue(len(posts)>0)
        
    def test_update_caption(self):
        self.post.save_post()
        self.post.update_post_caption(self.post.id,'test')
        updated= Image.objects.get(caption='test')
        self.assertEqual(updated.caption,'test') 
        
    def test_delete_post(self):
        self.post.save_post()
        self.post.delete_post()
        posts=Image.objects.all()
        self.assertTrue(len(posts)==0)              

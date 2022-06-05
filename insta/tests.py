from django.test import TestCase
from .models import Profile, Comments, Image, User

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        self.user.save()
        self.user_profile = Profile(user=self.user,image="mypic.png")
        self.post = Image(name="views",caption="my views",user=self.user_profile)
        
    def tearDown(self):
        Image.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.all().delete()
        
    def test_instance(self):
        self.assertTrue(isinstance(self.post,Image))
            
    def test_save_post(self):
        self.post.save_image()
        posts=Image.objects.all()
        self.assertTrue(len(posts)>0)
        
    def test_delete_post(self):
        self.post.save_image()
        self.post.delete_image()
        posts=Image.objects.all()
        self.assertTrue(len(posts)==0)   

class CommentsTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        self.user.save()
        self.user_profile = Profile(user=self.user,image="mypic.png")
        self.post = Image(name="views",caption="my views",user=self.user_profile)
        self.post.save()
        self.comment = Comments(comment="Awsome",post=self.post,user=self.user)
        
    def tearDown(self):
        Image.objects.all().delete()
        User.objects.all().delete()
        Comments.objects.all().delete()
        Profile.objects.all().delete()
                    
    def test_instance(self):
        self.assertTrue(isinstance(self.comment,Comments))

    def test_delete_comment(self):
        self.comment.save_comment()
        self.comment.delete_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)==0) 

    def test_save_comment(self):
        self.comment.save_comment()
        comments=Comments.objects.all()
        self.assertTrue(len(comments)>0)

class ProfileTestClass(TestCase):
    def setUp(self):
        self.user = User(username='alex')
        
        self.user_profile = Profile(user=self.user,image="mypic.png")
   
    def tearDown(self):
        User.objects.all().delete()
        Profile.objects.all().delete()
      
    def test_instance(self):
        self.assertTrue(isinstance(self.user_profile,Profile))
            
    def test_save_user_profile(self):
        self.user_profile.save_profile()
        profiles=Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = models.ImageField(default='default.jpg', upload_to='profile_pics')
  bio = models.TextField(max_length=500, default='My Bio', blank=True)
  name = models.CharField(max_length=250, blank=True)
  
  def __str__(self):
    return f'{self.user.username} Profile'

  # def save(self): 
  #   super().save() 

  #   img = Image.open(self.image.path)

  #   if img.height > 300 or img.width > 300:
  #     output_size = (300, 300)
  #     img.thumbnail(output_size)
  #     img.save(self.image.path)

  def save_profile(self):
    self.user

  def delete_profile(self):
    self.delete()

  @classmethod
  def filter_profile_by_id(cls, id):
    profile = Profile.objects.filter(user_id = id).first()
    return profile

  @classmethod
  def search_profile(cls, name):
    return cls.objects.filter(user__username__icontains=name).all()

class Image(models.Model):
  image =models.ImageField(upload_to = 'uploads/')
  name = models.CharField(max_length=250, blank=True)
  caption = models.CharField(max_length=250, blank=True)
  likes = models.ManyToManyField(User, related_name='likes', blank=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
  created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return f'{self.user.name} Post'




  



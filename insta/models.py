from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  image = CloudinaryField('profile_pics/',default='default.jpg')
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
  image = CloudinaryField('uploads/')
  name = models.CharField(max_length=250, blank=True)
  caption = models.CharField(max_length=250, blank=True)
  likes = models.ManyToManyField(User, related_name='likes', blank=True)
  user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='posts')
  created = models.DateTimeField(auto_now_add=True, null=True)

  class Meta:
    ordering = ['-pk']

  def save_image(self):
    self.save() 

  def delete_image(self):
    self.delete()

  def total_likes(self):
    return self.likes.count()

  @classmethod
  def get_profile_posts(cls, profile):
    posts = Image.objects.filter(profile__pk = profile)
    return posts 

  @classmethod
  def update_image_caption(cls, id, caption):
    update = cls.objects.filter(id = id).update(caption = caption)
    return update        

  def __str__(self):
    return f'{self.user.name} Post'

class Comments(models.Model):
  comment = models.CharField(max_length=100)
  post=models.ForeignKey(Image,related_name='comments', on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
  created = models.DateTimeField(auto_now_add=True, null=True)

  def __str__(self):
    return f'{self.comment} Image'
    
  def save_comment(self):
    self.save()
    
  def delete_comment(self):
    self.delete()
    
  @classmethod
  def filter_comments_by_post_id(cls, id):
    comments = Comments.objects.filter(post__id=id)
    return comments
    

  class Meta:
    ordering = ["-pk"]


class Follow(models.Model):
  follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
  followed = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')

  def __str__(self):
      return f'{self.follower} Follow'







  



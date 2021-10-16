from django.db import models
from django.utils import timezone
#ユーザー認証
from django.contrib.auth.models import User

#ユーザーアカウントのモデルクラス
class Account(models.Model):

    #ユーザー認証のインスタンス(1vs1関係)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Lists(models.Model):
    list_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    list_title = models.TextField()
    list_discription = models.TextField(blank = True, null = True)
    or_list_public = models.BooleanField(default='False')
    or_list_share = models.BooleanField(default='False')

class Posts(models.Model):
    post_id = models.AutoField(primary_key=True)
    list_id = models.ForeignKey('myhp.lists', on_delete=models.CASCADE)
    user_id = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    latitude = models.TextField()
    longitude = models.TextField()
    address = models.TextField()
    place_name = models.TextField()
    post_title = models.TextField()
    post_discription = models.TextField(blank = True, null = True)
    post_image = models.ImageField(upload_to='images',blank=True, null=True)
    post_link = models.TextField(blank = True, null = True)
    post_date = models.TextField(blank = True, null = True)
    post_hashtag = models.TextField(blank = True, null = True)
    or_datail = models.BooleanField(default='False')
    or_post_share = models.BooleanField(default='False')
    updated_time = models.DateTimeField(default=timezone.now)
    created_time = models.DateTimeField(default=timezone.now)

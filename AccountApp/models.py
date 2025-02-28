# from django.db import models
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth.hashers import check_password

# # Create your models here.

# class User(models.Model):
#     avatarUrl = models.URLField(default='https://static.vecteezy.com/system/resources/previews/009/292/244/non_2x/default-avatar-icon-of-social-media-user-vector.jpg')
#     username = models.CharField(max_length=100)
#     email = models.EmailField()
#     password = models.CharField(max_length=100)
#     created_at = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.username
    
#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)

#     def check_password(self, raw_password):
#         return check_password(raw_password, self.password)

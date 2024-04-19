from django.db import models

#ユーザテーブル
class User(models.Model):
    username = models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=20)
    is_active = models.BooleanField(default=False)
    is_delete = models.BooleanField(default=True)
    def __str__(self):
        return self.username


#合言葉
class Aikotoba(models.Model):
    aikotoba = models.CharField(max_length=30,unique=True)
    def __str__(self):
        return self.aikotoba
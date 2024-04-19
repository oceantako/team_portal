from django.db import models

class HumansImage(models.Model):
    picture = models.ImageField(upload_to='team_member_img/')
    title = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.title

class MemberWorks(models.Model):
    member = models.CharField(max_length=200)
    date = models.DateTimeField()
    title = models.CharField(max_length=200,unique=True)
    picture = models.ImageField(upload_to='members_work/images')
    link = models.CharField(max_length=2100, null=True, blank=True)
    file = models.FileField(upload_to='members_work/files', null=True, blank=True)
    explanation = models.TextField()
    is_delete = models.BooleanField(default=False)

    def __str__(self):
        return self.title


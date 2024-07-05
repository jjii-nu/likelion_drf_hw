from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

def image_upload_path(instance, filename):
    return f'{instance.singer.pk}/{filename}'
class Singer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(max_length=20, default='Unknown')
    content = models.TextField()
    debut = models.DateField()
    tag = models.ManyToManyField(Tag, blank=True)
    #image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)

#다중이미지 구현코드
class Image(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to=image_upload_path, blank=True, null=True)
#여기까지
class Song(models.Model):
    id = models.AutoField(primary_key=True)
    singer = models.ForeignKey(Singer, blank=False, null=False, on_delete=models.CASCADE, related_name='songs')
    release = models.DateField()
    content = models.TextField()
from django.db import models

from django.conf import settings
from django.db import models
from django.utils import timezone

class Place_info(models.Model):
    author = models.CharField(max_length=20)                    #작성자
    title = models.CharField(max_length=200)                    #제목
    lat = models.FloatField()                                   #위도
    lng = models.FloatField()                                   #경도
    road_adr = models.CharField(max_length=500)                 #도로명주소
    num_adr = models.CharField(max_length=500)                  #지번주소
    tel = models.CharField(max_length=13)                       #전화번호
    created_date = models.DateTimeField(
        blank=True, null=True) #작성일시
    
    def publish(self):
        self.created_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

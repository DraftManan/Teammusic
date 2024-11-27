from django.db import models

# Create your models here.
from django.db import models
import uuid
from django.urls import reverse


# โมเดล Singer
class Singer(models.Model):
    name = models.CharField(max_length=100)                # ชื่อนักร้อง
    genre = models.CharField(max_length=50, blank=True, null=True)  # แนวเพลง (Pop, Rock, Jazz ฯลฯ)
    birth_date = models.DateField(blank=True, null=True)    # วันเกิดนักร้อง
    country = models.CharField(max_length=50, blank=True, null=True) # ประเทศที่นักร้องมาจาก
    biography = models.TextField(blank=True, null=True)     # ประวัตินักร้อง
    s3_photourl = models.ImageField(upload_to='img/', blank=True, null=True)
    
    def __str__(self):
        return self.name

# โมเดล Album
class Album(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="albums") # ลิงก์ไปยัง Singer
    title = models.CharField(max_length=100)              # ชื่ออัลบั้ม
    release_date = models.DateField(blank=True, null=True) # วันที่ปล่อยอัลบั้ม
    s3_alblumurl = models.ImageField(upload_to='img/', blank=True, null=True)

    def __str__(self):
        return self.title

# โมเดล Song
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="songs") # ลิงก์ไปยัง Album
    title = models.CharField(max_length=100)                # ชื่อเพลง
    duration = models.TimeField(blank=True, null=True)      # ระยะเวลาเพลง
    genre = models.CharField(max_length=50, blank=True, null=True) # แนวเพลง
    release_date = models.DateField(blank=True, null=True)  # วันที่ปล่อยเพลง (ถ้ามี)
    s3_url = models.URLField(max_length=5000, blank=True, null=True) # URL ของไฟล์เพลงที่เก็บใน S3
    
    def __str__(self):
        return self.title

from django.db import models

class Playlist(models.Model):
    name = models.CharField(max_length=100)     # ชื่อ Playlist
    description = models.TextField(blank=True, null=True)   # คำอธิบายเกี่ยวกับ Playlist (optional)
    cognito_user_id = models.CharField(max_length=100, blank=True, null=True)  # เจ้าของ Playlist (Cognito User ID)
    songs = models.ManyToManyField('Song', related_name="playlists", blank=True)     # เพลงที่อยู่ใน Playlist (Many-to-Many Relationship)
    playlist_image = models.ImageField(upload_to='playlist/', blank=True, null=True)
    share_token = models.UUIDField(default=uuid.uuid4, unique=True)

    def __str__(self):
        return self.name

    def get_share_url(self):
        # สร้าง URL สำหรับแชร์โดยใช้ share_token
        return reverse("share_playlist", args=[str(self.share_token)])
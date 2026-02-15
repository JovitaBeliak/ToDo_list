from django.contrib.auth.models import AbstractUser
from django.db import models
from PIL import Image
from django.utils import timezone
from tinymce.models import HTMLField


# Create your models here.
class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to='profile_pics', null=True, blank=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.photo:
            img = Image.open(self.photo.path)
            min_side = min(img.width, img.height)
            left = (img.width - min_side) // 2
            top = (img.height - min_side) // 2
            right = left + min_side
            bottom = top + min_side
            img = img.crop((left, top, right, bottom))
            img = img.resize((300, 300), Image.LANCZOS)
            img.save(self.photo.path)


class Task(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100)
    description = HTMLField(verbose_name="Description", max_length=3000)
    doer = models.ForeignKey(to='TodoList.CustomUser', verbose_name="Doer",
                               on_delete=models.SET_NULL,
                               null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    STATUS = (
        ('s', 'Sukurta'),
        ('v', 'Vykdoma'),
        ('u', 'Užbaigta'),
    )
    status = models.CharField(choices=STATUS, default='s')

    def is_overdue(self):
        return self.due_date and timezone.now().date() > self.due_date

    def __str__(self):
        return f'{self.title}, Vykdytojas: {self.doer}'


class TaskReview(models.Model):
    task = models.ForeignKey(to='Task', on_delete=models.SET_NULL, null=True, blank=True)
    reviewer = models.ForeignKey(to='TodoList.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    class Meta:
        ordering = ['-date_created']
from django.db import models

# Create your models here.

class Post(models.Model) :
    title = models.CharField(max_length=40)
    content = models.TextField(max_length=500)
    image = models.ImageField(upload_to="media", blank=True, default="./static/myapp/images/django.png")
    publish_date = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Category(models.TextChoices):
       Frontend = "Frontend"
       Backend = "Backend"
       Fullstack = "Fullstack"
    category = models.CharField(max_length=9, choices=Category.choices,default=Category.Frontend)

    class Status(models.TextChoices):
       Draft = "Draft"
       Published = "Published"
    status = models.SlugField(max_length=9, choices=Status.choices, default=Status.Draft)
    slug = models.IntegerField(max_length=20)


    def __str__(self):
        return f"{self.title} - {self.content} - {self.image} - {self.publish_date} - {self.last_update} - {self.category} - {self.status} - {self.slug}"

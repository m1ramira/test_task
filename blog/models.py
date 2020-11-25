from django.db import models

# Create your models here.
class User(models.Model):
    """
    Модель "Пользователь", включающая в себя
    имя пользователя, его почта, телефон, адрес и др.
    """
    name = models.CharField(max_length=254)
    username = models.CharField(max_length=254)
    email = models.EmailField(max_length=254)
    street = models.CharField(max_length=254)
    suite = models.CharField(max_length=254)
    city = models.CharField(max_length=254)
    zipcode = models.CharField(max_length=254)
    lat = models.FloatField()
    lng = models.FloatField()
    phone = models.CharField(max_length=254)
    website = models.URLField()
    company_name = models.CharField(max_length=254)
    catch_phrase = models.TextField()
    bs = models.CharField(max_length=254)




class Post(models.Model):
    """
    Модель "Пост", включающая в себя связь с user_id (один-ко-многим),
    наименование поста и текст поста
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=254)
    body = models.TextField()








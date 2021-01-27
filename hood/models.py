from django.db import models
from django.contrib.auth.models import User
import datetime as dt


class Profile(models.Model):
    bio = models.TextField(max_length=100,blank=True)
    profilepic = models.ImageField(upload_to='profile/',blank= True)
    email = models.CharField(blank=True, max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user

class Neighbourhood(models.Model):
    Neighbourhood = models.CharField(max_length=30, null=True)
    Neighbourhood_location = models.CharField(max_length=30, null=True)
    population = models.PositiveIntegerField(default=0)
    police_no = models.PositiveIntegerField(default=112)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.Neighbourhood

    def create_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()

    @classmethod
    def get_neighbourhoods(cls):
        estates = Neighbourhood.objects.all()
        return estates

    @classmethod
    def get_specific_hood(cls, id):    
        chosen_hood = cls.objects.get(id=id)
        return chosen_hood

    def find_neighbourhood(neighbourhood_id):
        query = cls.objects.filter(name_icontains = search_term)
        return query

class Follow(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    estates = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    @classmethod
    def get_following(cls, user_id):
        following = Follow.objects.filter(user=user_id).all() 
        return following   


class Business(models.Model):
    image = models.ImageField(upload_to = 'business/', null=True, blank=True)
    project = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=70, blank=True)
    estate = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)

    def __str__(self):
        return self.project

    @classmethod
    def get_bussinesses(cls):
        business = cls.objects.all()
        return business

    @classmethod
    def get_bussiness_by_estate(cls, neighbourhood_id):
        messages = cls.objects.all().filter(estate = neighbourhood_id) 
        return messages


class Post(models.Model):
    image = models.ImageField(upload_to='photos/', null=True)
    image_name = models.CharField(max_length=30)
    message = models.TextField(max_length=100, null=True, blank=True)
    estate = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, null=True)
    user_profile = models.ForeignKey(Profile, on_delete = models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE)


    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete

    @classmethod
    def get_posts(cls):
        messages = cls.objects.all()     


    @classmethod
    def get_posts_by_estate(cls, neighbourhood_id):
        messages = cls.objects.filter(estate=neighbourhood_id)
        return messages       
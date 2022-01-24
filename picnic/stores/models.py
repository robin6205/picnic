from django.db import models

# Create your models here.
# for anytime I want to pass data
# needs to be connected to frontend and database

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Restaurant(models.Model):

    # def clean_name(self):
    #    cleaned_data = self.clean()
    #    return cleaned_data.get('restaurant_name')

    restaurant_name = models.CharField(max_length=200)
    store_page = models.URLField(max_length = 200, default = '')
    store_page = models.FilePathField(max_length=200, default=' ')

    imageurl = 'uploads/'
    image = models.ImageField(upload_to =imageurl, height_field=None, width_field=None, max_length=100)
    
    def __str__(self):
        return self.restaurant_name

# class PageData(models.Model):
#     restaurantSelected 
# class RestaurantImage(models.Model, restaurantInstance):
#     url = restaurantInstance.clean_name()
#     image = models.ImageField(upload_to =url, height_field=None, width_field=None, max_length=100)
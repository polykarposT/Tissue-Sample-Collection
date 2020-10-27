# Tissue-Sample-Collection
Tissue Sample Collection Wep App an administrative interface for a system that allow
a Tissue Sample directory to keep track of the number of samples with certain characteristics
contained within a larger collection of samples.


## Requirements
To be able to run the project need to have installed python (python >= 3.8) and Django framework (3.1.2). Django framework can be install via pip:
```
pip install Django
```

## Start Project
In the directory that you want to create the project open a terminal or command line and write:
```
django-admin startproject tissue_sample
```
Tissue_sample is the name of the project

After this command you will be able to see in the directory a new folder with the name of the projet. Get in the folder.
```
cd tissue_sample
```

In the folder there are an another folder with tha same name as the project(tissue_sample) and manage.py file.
Let's verify your Django projects works.Run the following command:
```
python manage.py runserver  or
python3 manage.py runserver
```
Now that the server’s running, visit http://127.0.0.1:8000/ with your Web browser. You’ll see a “Congratulations!” page, with a rocket taking off. It worked!

## Create App
To create your app, make sure you’re in the same directory as manage.py and type this command:
```
python manage.py startapp tissue_collection
```
That’ll create a directory tissue_collection, which is laid out like this:
```
tissue_collection/
    __init__.py
    admin.py
    apps.py
    migrations/
        __init__.py
    models.py
    tests.py
    views.py
```
Now open settings.py and add the tissue_collection project
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tissue_collection',
    'django_filters',
]

```
## Models
This project uses the default database which is SQLite. In tissue_collection directory and in the models.py file add the following code to describe what the web app will store in the databae. Models are the tables in the database.
```
from django.db import models

# Create your models here.

class Collection(models.Model):
    desease_term = models.CharField(max_length=250)
    title = models.CharField(max_length=250)

    #Return objects by desease_term for example "Test 1" and not like "Collection.objects.(1)"
    def __str__(self):
        return self.desease_term

class Sample(models.Model):
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    donor_count = models.IntegerField()
    material_type = models.CharField(max_length=250)
    last_updated = models.DateField()

    def __str__(self):
        return str(self.id)


```
The variables in every class are actually the columns of the tables. Inside the classes we added the ``` def __str__``` function to return the data by desease_term. The reason is for readability perpuse because is better to see "Test 1" from "<Collection: Collection object(1)".
If you watch carefully you will see that we didn't add a primary key and the reason is bacause Django is doing it automatically. Of course it's only if you want to primary keys like 1,2,3.

Django provides an admin page and the phylosophy is to generating admin sites to add, change, and delete content is tedious work that doesn’t require much creativity. For that reason, Django entirely automates creation of admin interfaces for models. To use this featrure you need to do 3 easy steps.

1) go to admin.py and add the following code:
```
from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Collection)
admin.site.register(Sample)

```
2) In the same directory with ```manage.py``` file run the following commands in terminal:
```
python manage.py makemigrations 
python manage.py migrate #create database for the project as we defined it the models.py file

python manage.py createsuperuser #to use admin pane you need to create an admin account
```
3) You are ready! Now visit  http://127.0.0.1:8000/admin/ and login with the username and password you add. In this project the credentials are:
```
username: testUser
password: test1234
```
Now you can add data from here!

## HTML Templates
In the tissue_collection directory create a new folder with name ```templates``` and inside templates folder create a new folder with name ```collection```. There are all the html code for the project.

Create a ```base.html``` file which has all the bootstrap and javascript libraries we need for the project. Django use jinga for frint end so we will use ```{{ }}``` to print data and ```{% %}``` to make for loops, if statement, django urls and build block content.

## Views
In views.py file we create all the neccasary functions to make projects working. In views you can handle data, make queries and forms and render html templates. To make views workind we need to create a ```urls.py```file in the tissue_collection directory. After we created the file add the following code:
```
from django.urls import path
from . import views

#URLs that will call our views 
# For example if you want to retrive all samples you will write in the url 127.0.0.1:8000/samples/
# django automatically will try to match url with an existing view
 
urlpatterns = [
    path('', views.index, name='index'),
    path('samples/', views.samples, name='samples'),
    path('samples/<int:sample_id>/', views.sample, name='sample'),
    path('samples/<int:sample_id>/update/', views.update_sample, name='update_sample'),
    path('sample/<int:sample_id>/delete/', views.delete_sample, name='delete_sample'),
    path('collection/<int:collection_id>/', views.collection, name='collection'),
    path('collection/<int:collection_id>/create_sample/', views.create_sample, name='create_sample'),
    path('collection/<int:collection_id>/update/', views.update_collection, name='update_collection'),
    path('collection/<int:collection_id>/delete/', views.delete_collection, name='delete_collection'),
    path('create_collection/', views.create_collection, name='create_collection'),
]
```
Don't worry for now all those paths are the urls of the projects. We will see them in a while.
Now your need to open ```urls.py``` from tissue_sample folder and include the urls from tissue_collection folder. So in the urls.py of tissue_sample add:
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tissue_collection.urls')),
]
```

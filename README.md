# Tissue-Sample-Collection
Tissue Sample Collection Web App is an administrative interface for a system that allows
a Tissue Sample directory to keep track of the number of samples with certain characteristics
contained within a larger collection of samples.


## Requirements
To be able to run the project you need to have installed python (python >= 3.8) and Django framework (3.1.2). Django framework can be installed via pip:
```
pip install Django
```
For this project you also need to install django-filters.
```
pip install django-filter
```

## Start Project
In the directory that you want to create the project open a terminal or command line and write:
```
django-admin startproject tissue_sample
```
Tissue_sample is the name of the project.

After this command you will be able to see in the directory a new folder with the name of the project. In order to get in the folder type:
```
cd tissue_sample
```

In the folder there is an another folder with the same name as the project(tissue_sample) and a manage.py file.
Let's verify your Django project works.Run the following command:
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
## Forms
Create a ```forms.py``` in the tissue_collection directory.In the forms.py file create 3 forms to create and Update Collections and Samples.
Django forms is used because it provides functions to validate form data easily.
```
from django import forms
from .models import Collection, Sample

#create forms for create, and update collections and samples
 
class CollectionForm(forms.ModelForm):
    class Meta:
        model = Collection #which model represents 
        fields = ('title', 'desease_term')
        #adding bootstrap class to form fields
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title', 'required': 'true', 'type': 'text'}),
            'desease_term': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Desease term', 'required': 'true', 'type': 'text'}),
        }

class SampleForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('donor_count','material_type')
        widgets = {
            'donor_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90152', 'required': 'true', 'type': 'number', 'min':'0'}),
            'material_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Cerebrospinal fluid"', 'required': 'true', 'type': 'text'})
        }


class SampleUpdateForm(forms.ModelForm):
    class Meta:
        model = Sample
        fields = ('collection','donor_count', 'material_type')
        widgets = {
            'collection': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Select collection', 'required': 'true'}),
            'donor_count': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '90152', 'required': 'true', 'type': 'number', 'min': '0'}),
            'material_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '"Cerebrospinal fluid"', 'required': 'true', 'type': 'text'})
        }
```
To create forms you need to make class with the name you wish, adding 'Form' at the end. Inside the form class you declare which model this form refers to and the fields you want to be demostrated in the template. Widgets will help you pass bootstrap classes.You will use the forms in views.py of the project so you need to add them in that file.
```from .forms import CollectionForm, SampleForm, SampleUpdateForm```
The last thing to do before you start building views functions is to create a django filter for search purposes.

## Filters
Django-filter provides a simple way to filter down a queryset based on parameters the user provides. You need to add it to ```settings.py``` file where you previously added ```tissue_collection```.
Filters and forms are almost the same. Create a file in the tissue_collection directory with the name ```filters.py``` and add
```
import django_filters
from django import forms
from .models import *

#create filter to help search for collection.

class CollectionFilter(django_filters.FilterSet):
    class Meta:
        #this filter will search for collections
        model = Collection

        fields = ['title', 'desease_term']
        #use filter overrides to calls widget to pass boostrap classes
        filter_overrides = {
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
                },
            },
            models.CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'widget': forms.TextInput(attrs={'class': 'form-control', 'type': 'text'}),
                },
            },
        }
```
It's exactly the same with forms but instead of using widget here you use filter_overrides to add bootstrap classes.

## Models
This project uses the default database which is SQLite. In tissue_collection directory and in the models.py file add the following code to describe what the web app will store in the database. The Models are the tables in the database.
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
The variables you declare in every class are actually the columns of the tables. Inside the classes you add the ``` def __str__``` function to return the data by desease_term and sample ID for readability purposes because it is better to return "Test 1" than "<Collection: Collection object(1)>".
If you watch carefully you will notice that you didn't add a primary key and the reason for that is that Django is doing it automatically for you. Naturally, that's the case only if you want the primary key to be in numeric form, like 1,2,3.

Django provides an admin page and the philosophy is to generate admin sites to add, change, and delete content which is a tedious work that doesn’t require much creativity. For this reason, Django entirely automates creation of admin interfaces for models. To use this featrure you need to follow 3 easy steps.

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
python manage.py migrate #create database for the project as you defined it the models.py file

python manage.py createsuperuser #to use admin pane you need to create an admin account
```
3) You are ready to go! Now visit  http://127.0.0.1:8000/admin/ and login with the username and password you added. In this project the credentials are:
```
username: testUser
password: test1234
```
Now you can add data from here!

## HTML Templates
In the tissue_collection directory create a new folder with the name ```templates``` and inside the templates folder create a new folder with the name ```collection```. There you will find the entire html code for the project.

Create a ```base.html``` file which has all the bootstrap and javascript libraries you need for the project. Django uses jinja for front end so you will use ```{{ }}``` to print data and ```{% %}``` to make loops, if-statements, django-urls and to build block contents.

For example, if you have a ```<a href=""></>``` tag and you want to go to another page such as the all samples the tag will look this ```<a href="{% url 'samples' %}">All samples</a>```

To use the view function with the ID argument the tag will be ``` <a href="{% url 'sample' sample_id= sample.id %}"```. Sample_id will be the name appearing in your urls as well as the argument in sample view.

## Views & URLS
In views.py file you create all the necessary functions to make the project work. In views you can handle data, make queries and forms and render html templates. To make views work you need to create a ```urls.py```file in the tissue_collection directory. After you create the file add the following code:
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
Path contains the url, for example ```samples/```, a view function that performs an action and a name for this path that you will use in html templates for the url .
All those paths are the urls of the project.
Now you need to open ```urls.py``` from tissue_sample folder and include the urls from the tissue_collection folder. In the urls.py of tissue_sample add:
```
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tissue_collection.urls')),
]
```

### Index function view
Index function takes as argument a request (POST or GET) and returns an html template and a context which has all the data, meaning the form to create new collection, all collections and collections filter for the search form.
```
def index(request):
    form = CollectionForm() #create collection form
    collections = Collection.objects.all() # retrieve all collections from database
    collections_filter = CollectionFilter(request.GET, queryset=collections) #filter that takes arguments request.GET method because is search and collection query
    collections = collections_filter.qs #filtered collection query
    context = {'collections': collections, 'form': form, 'collections_filter': collections_filter} #build our context with data to print them in front end
    return render(request, 'collection/index.html', context) #return our index page with context data
```
URL= ```index```

### Samples function view
Returns all samples
```
def samples(request):
    samples = Sample.objects.all() #return all samples
    context = {'samples': samples}
    return render(request, 'collection/samples.html', context)
```
URL ```samples/```

### Sample function view
Takes as arguments a request and a sample_id and returns all the information of the sample with this id.
```
def sample(request,sample_id):
    sample = get_object_or_404(Sample, id=sample_id) #return sample with id = sample_id or throw 404
    context = {'sample': sample}
    return render(request, 'collection/sample.html', context)
```
The url for this function is ```sample/<int:sample_id/>```. The int in the url is to let django know that there is an argument which is int.

### Collection function view
Takes as arguments a request and a sample_id and returns all the information of the collection with this id
```
def collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id) #return collection with id=collection_id or 404
    samples = collection.sample_set.all() #return all samples which related with this collection
    sample_form = SampleForm() #create sample for this collection
    context = {'collection': collection, 'samples': samples, 'sample_form': sample_form,}
    return render(request, 'collection/collection.html', context)
```
URL= ```collection/<int:collection_id>/```

### Create collection function view
Creates a collection. Because you created the CollectionForm previously, django will handle the data for you. 
```
desease_term    text not null
title           text not null
```
```
def create_collection(request):

    if request.method == "POST": #check if the request of the form is POST
        form = CollectionForm(request.POST) #this form has request method
        if form.is_valid(): # default function from django to check if data of a form are valid
            desease_term = request.POST['desease_term'] 
            title = request.POST['title']
            
            collection = Collection(desease_term=desease_term, title=title) #create new object with the given values
            collection.save() #save this object to database
            return redirect('index') # if everything is ok return to index
        else:
            messages.error(request, 'Please enter valid information') #if form is not valid throw error message
            return redirect('index')
    else:
        form = CollectionForm()
        collections = Collection.objects.all()
        context = {'collections': collections, 'form': form}
        return render(request, 'collection/index.html', context)
```
URL = ```create_collection/```

### Update Collection function view
Updates an existing collection with specific id. To execute the function you need to pass the collection_id and in the update form, django will handle everything as mentioned before.
```
desease_term    text not null
title           text not null
```
```
def update_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id) #return collection with id = collection_id or 404
    form = CollectionForm(instance=collection) #in the same create collection form check if collection exist and put this collection data into the form
    if request.method == "POST": #check if method is POST
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid(): #check if form is valid
            form.save()
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
        else:
            messages.error(request, 'Please enter valid information')
    context = {'form': form, 'collection': collection}
    return render(request, 'collection/update_collection.html', context)
```
URL = ```collection/<int: collection_id>/update/```

### Delete collection function view
Deletes a collection with specific id. If you delete this function you also delete all the samples of this collection.
```
def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id) #return collection wiht specific id of 404
    samples = collection.sample_set.all() #if you delete a colletion you will delete also all collection's samples
    if request.method == "POST": #check if method is POST to delete collection
        collection.delete()
        return redirect('index')

    context = {'collection': collection, 'samples': samples}
    return render(request, 'collection/delete_collection.html', context)
    
```
URL = ```collection/<int: collection_id>/update/```

### Create Sample function view
Creates a Sample for an existing collection. You can create new sample only when you are in the details of an existing collection. Here again djnago will automatically handle everything. You will to pass in the function the collection id in order to use it as a foreign key.
```
donor_count     int not null not negative
material_type   text not null
```
The last updated field will be handled from the database.

```
def create_sample(request, collection_id):
    collection = Collection.objects.get(id=collection_id) #return collection with id = collection_id
    date_now = datetime.datetime.now() #retrieve current date
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            donor_count = request.POST['donor_count']
            material_type = request.POST['material_type']
            #save new sample for this collection
            sample = Sample(collection=collection, donor_count=donor_count,
                            material_type=material_type, last_updated=date_now)
            sample.save()
            #if everything is ok return to this specific collection. you need to use reverse to pass collection id to be able to redirect
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
        else:
            messages.error(request, 'Please enter valid information')
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))

    return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
```
URL = ```collection/<int:collection_id>/create_sample/```

### Update Sample function view
Updates a sample with specific id(sample_id).
```
def update_sample(request, sample_id):
    sample = get_object_or_404(Sample, id=sample_id) #return sample with id = sample_id or 404
    date_now = datetime.datetime.now() #retrieve current date
    form = SampleUpdateForm(instance=sample) #pass sample to update form to have access of it's data
    if request.method == "POST":  #check if method is POST
        form = SampleUpdateForm(request.POST, instance=sample)
        if form.is_valid(): #check if method is POST
            # commit=False tells Django that "Don't send this to database yet.
            sample = form.save(commit=False)
            #updating last_updated field in database
            sample.last_updated = date_now
            sample.save()
            return redirect(reverse('sample', kwargs={'sample_id': sample_id}))
        else:
            messages.error(request, 'Please enter valid information')
    context = {'form': form, 'sample':sample}
    return render(request, 'collection/update_sample.html', context)
```
URL = ```sample<int: sample_id>/update/```

### Delete Sample function view
Deletes a sample with specific id.
```
def delete_sample(request, sample_id):
    sample = get_object_or_404(Sample, id=sample_id)
    collection_id = sample.collection.id #keep collection id of the sample to redirect to this collection after delete the sample
    if request.method == "POST":
        sample.delete()
        return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
    
    context = {'sample': sample}
    return render(request, 'collection/delete_sample.html', context)
```
URL = ```sample/<int: sample_id>/delete/```

## EXECUTE THE PROJECT
Download repo using ```git clone ``` or if you have the zip file unizip it in the directory you want.
To run the project you need to have python (python >=3.8), Django Framework(3.1.2) and django-filters installed before you run the project. After that, in the same directory with ```manage.py``` file run the following command :
```python manage.py runserver```
If you have python 2 and python 3 in your system and python3 is not the default maybe you will need to run :
```python3 manage.py runserver```
Now you are ready to visit 127.0.0.1:8000!

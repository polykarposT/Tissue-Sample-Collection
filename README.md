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
That’ll create a directory polls, which is laid out like this:
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

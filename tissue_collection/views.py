from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import *
from .forms import CollectionForm, SampleForm, SampleUpdateForm
from .filters import CollectionFilter
import datetime
# Create your views here.

def index(request):
    form = CollectionForm()
    collections = Collection.objects.all()
    collections_filter = CollectionFilter(request.GET, queryset=collections)
    collections = collections_filter.qs
    samples = Sample.objects.all()
    context = {'collections': collections, 'form': form, 'collections_filter': collections_filter, 'samples': samples}
    return render(request, 'collection/index.html', context)

def samples(request):
    form = SampleForm()
    samples = Sample.objects.all()
    context = {'samples': samples, 'form': form}
    return render(request, 'collection/samples.html', context)

def sample(request,sample_id):
    sample = get_object_or_404(Sample, id=sample_id)
    context = {'sample': sample}
    return render(request, 'collection/sample.html', context)

def collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    samples = collection.sample_set.all()
    sample_form = SampleForm()
    context = {'collection': collection, 'samples': samples, 'sample_form': sample_form,}
    return render(request, 'collection/collection.html', context)


def create_collection(request):

    if request.method == "POST":
        form = CollectionForm(request.POST)
        if form.is_valid():
            desease_term = request.POST['desease_term']
            title = request.POST['title']
            
            collection = Collection(desease_term=desease_term, title=title)
            collection.save()
            return redirect('index')
        else:
            messages.error(request, 'Please enter valid information')
            return redirect('index')
    else:
        form = CollectionForm()
        collections = Collection.objects.all()
        context = {'collections': collections, 'form': form}
        return render(request, 'collection/index.html', context)

def update_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    form = CollectionForm(instance=collection)
    if request.method == "POST":
        form = CollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
        else:
            messages.error(request, 'Please enter valid information')
    context = {'form': form, 'collection': collection}
    return render(request, 'collection/update_collection.html', context)


def delete_collection(request, collection_id):
    collection = get_object_or_404(Collection, id=collection_id)
    samples = collection.sample_set.all()
    if request.method == "POST":
        collection.delete()
        return redirect('index')

    context = {'collection': collection, 'samples': samples}
    return render(request, 'collection/delete_collection.html', context)


def create_sample(request, collection_id):
    collection = Collection.objects.get(id=collection_id)
    date_now = datetime.datetime.now()
    if request.method == "POST":
        form = SampleForm(request.POST)
        if form.is_valid():
            donor_count = request.POST['donor_count']
            material_type = request.POST['material_type']

            sample = Sample(collection=collection, donor_count=donor_count,
                            material_type=material_type, last_updated=date_now)
            sample.save()
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
        else:
            messages.error(request, 'Please enter valid information')
            return redirect(reverse('collection', kwargs={'collection_id': collection_id}))

    return redirect(reverse('collection', kwargs={'collection_id': collection_id}))


def update_sample(request, sample_id):
    sample = get_object_or_404(Sample, id=sample_id)
    date_now = datetime.datetime.now()
    form = SampleUpdateForm(instance=sample)
    if request.method == "POST":
        form = SampleUpdateForm(request.POST, instance=sample)
        if form.is_valid():
            # commit=False tells Django that "Don't send this to database yet.
            sample = form.save(commit=False)
            sample.last_updated = date_now
            sample.save()
            return redirect(reverse('sample', kwargs={'sample_id': sample_id}))
        else:
            messages.error(request, 'Please enter valid information')
    context = {'form': form, 'sample':sample}
    return render(request, 'collection/update_sample.html', context)


def delete_sample(request, sample_id):
    sample = get_object_or_404(Sample, id=sample_id)
    collection_id = sample.collection.id
    if request.method == "POST":
        sample.delete()
        return redirect(reverse('collection', kwargs={'collection_id': collection_id}))
    
    context = {'sample': sample}
    return render(request, 'collection/delete_sample.html', context)




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Word, WordCollection
from .forms import WordForm, WordCollectionForm

@login_required
def world_view(request):
    word_collections = WordCollection.objects.filter(public=True).all()
    return render(request, 'world.html', {
        'collections': word_collections
    })

@login_required
def clone_wordCollection(request, collectionId):
    original_collection = WordCollection.objects.get(id=collectionId)
    
    new_collection = WordCollection.objects.create(
        title=original_collection.title + " (Copy)", 
        language=original_collection.language,
        user=request.user, 
        public=original_collection.public
    )

    for word in original_collection.word_set.all():
        new_collection.word_set.create(
            word=word.word,
            translation=word.translation
        )

    return redirect('collections')

@login_required
def view_wordCollection_view(request, collectionId):
    collection = WordCollection.objects.get(id=collectionId)
    return render(request, 'view_wordCollection.html', {
        'collection': collection
    })

@login_required
def collections(request):
    word_collections = WordCollection.objects.filter(user=request.user).all()
    selected_collection_id = request.GET.get('collection')

    if selected_collection_id:
        try:
            selected_collection_id = int(selected_collection_id)
            selected_collection = get_object_or_404(WordCollection, id=selected_collection_id, user=request.user)
        except ValueError:
            selected_collection = None
            selected_collection_id = None
    else:
        selected_collection = None

    return render(request, 'collections.html', {
        'collections': word_collections,
        'selected_collection': selected_collection,
        'selected_collection_id': selected_collection_id,
    })

@login_required
def delete_collection(request, collection_id):
    collection = get_object_or_404(WordCollection, id=collection_id, user=request.user)
    collection.delete()
    messages.success(request, 'Collection deleted!')
    return redirect('collections')

@login_required
def add_collection(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        language = request.POST.get('language')
        public = request.POST.get('public') != None
        WordCollection.objects.create(user=request.user, title=title, language=language, public=public)
        messages.success(request, 'Collection added!')
        return redirect('collections')
    
    return render(request, 'add_collection.html')

@login_required
def add_word(request, collection_id):
    collection = get_object_or_404(WordCollection, id=collection_id, user=request.user)
    
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.save(commit=False)
            word.collection = collection
            word.save()
            messages.success(request, 'Word added successfully!')
            return redirect('collections')
    else:
        form = WordForm()

    return render(request, 'add_word.html', {'form': form, 'collection': collection})

@login_required
def edit_word(request, word_id):
    word = get_object_or_404(Word, id=word_id, collection__user=request.user)

    if request.method == 'POST':
        form = WordForm(request.POST, instance=word)
        if form.is_valid():
            form.save()
            messages.success(request, 'The word has been updated successfully!')
            return redirect('collections')
    else:
        form = WordForm(instance=word)

    return render(request, 'edit_word.html', {'form': form, 'word': word})

@login_required
def edit_collection(request, collection_id):
    collection = get_object_or_404(WordCollection, id=collection_id, user=request.user)

    if request.method == 'POST':
        form = WordCollectionForm(request.POST, instance=collection)
        if form.is_valid():
            form.save()
            messages.success(request, 'The collection has been updated successfully!')
            return redirect('collections')
    else:
        form = WordCollectionForm(instance=collection)

    return render(request, 'edit_collection.html', {'form': form, 'collection': collection})

@login_required
def delete_word(request, word_id):
    word = get_object_or_404(Word, id=word_id, collection__user=request.user)
    word.delete()
    messages.success(request, 'Word deleted!')
    return redirect('collections')

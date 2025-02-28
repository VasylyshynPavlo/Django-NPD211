from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Word, WordCollection
from .forms import WordForm 

@login_required
def collections(request):
    word_collections = WordCollection.objects.filter(user=2).all()
    print(word_collections.count())
    selected_collection_id = request.GET.get('collection')  # Отримуємо ID вибраної колекції

    if selected_collection_id:
        selected_collection = get_object_or_404(WordCollection, id=selected_collection_id, user=request.user)
    else:
        selected_collection = None

    return render(request, 'collections.html', {
        'collections': word_collections,
        'selected_collection': selected_collection,
        'selected_collection_id': selected_collection_id,
    })

@login_required
def add_collection(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        language = request.POST.get('language')
        WordCollection.objects.create(user=request.user, title=title, language=language)
        messages.success(request, 'Колекцію додано!')
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
            messages.success(request, 'Слово додано успішно!')
            return redirect('collections')  # Повертаємось до списку колекцій
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
            messages.success(request, 'Слово оновлено успішно!')
            return redirect('collections')
    else:
        form = WordForm(instance=word)

    return render(request, 'edit_word.html', {'form': form, 'word': word})

@login_required
def delete_word(request, word_id):
    word = get_object_or_404(Word, id=word_id, collection__user=request.user)
    word.delete()
    messages.success(request, 'Слово видалено!')
    return redirect('collections')

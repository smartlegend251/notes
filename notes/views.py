from django.shortcuts import render, redirect
from .models import *

def index(request):
    if request.method == 'POST':
        data = request.POST.get
        notes = data('notes')
        chapter = data('chapter')
        marks  = data('marks')
        print(notes)
        Notes.objects.create(
            chapter=chapter,
            notes=notes,
            marks = marks
        )
        return redirect('/')
    
    queryset = Notes.objects.all()
    
    chapter_names = {
        1: 'Introduction',
        2: 'Divide and Conquer',
        3: 'Greedy Method',
        4: 'Dynamic Programming',
        5: 'Basic Traversal & Search Techniques',
        6: 'Backtracking',
        7: 'Model Question Paper'
    }
    
    chapter_names_list = []
    for note in queryset:
        chapter = note.chapter
        chapter_name = chapter_names.get(chapter, 'Out of Context')
        chapter_names_list.append(chapter_name)
    zipped_data = zip(queryset, chapter_names_list)
    context = {'zipped_data': zipped_data}
    # context = {'notes': queryset, 'chapter_names': chapter_names_list}
    return render(request, 'home.html', context)


def checkup(request):
    if request.method == "POST":
        checked = request.POST.get('check')  # Assuming 'check' is a checkbox field
        ids = request.POST.get('ids')
        
        
        notes =Notes.objects.filter(id=ids).update(new_check=int(checked))
        # Notes.save()
        return redirect("/")
    
    

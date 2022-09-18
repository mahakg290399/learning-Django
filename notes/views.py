from django.shortcuts import render
from django.http import Http404
# Create your views here.

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    return render(request, 'notes/notes_list.html', {'notes':all_notes})

def notes_detail(request, pk):
    try:
        notes = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exists")
    return render(request, 'notes/notes_detail.html', {'notes':notes})
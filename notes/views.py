from django.shortcuts import render
from django.http import Http404
from django.views.generic import DetailView, ListView

# Create your views here.

from .models import Notes

class NoteslistView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "notes"


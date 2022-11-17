from django.shortcuts import render

from .models import Notes

def list(request):
    all_notes = Notes.objects.all()
    retrun render(request, 'notes/notes_list.html', {'notes' : all_notes})
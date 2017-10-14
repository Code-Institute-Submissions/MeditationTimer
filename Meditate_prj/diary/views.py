# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .forms import LogForm
from .models import DiaryEntry

# Create your views here.

# this view is a test & isn't working yet
def logform(request):
    if request.method == 'POST':
        form = LogForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = LogForm()
    return Http('logform.html', {'form':form},)

def entry_list(request):
    """
    Return all the diary entries and 
    render them to the diaryentries.html template
    """
    entries = DiaryEntry.objects.all()
    context = {'entries': entries}
    return render(request, "diaryentries.html", context)

def entry_detail(request, id):
    """
    Return a single diary entry based on
    the entry ID and render it to the 
    entrydetail.html template. Or return
    a 404 error
    """
    entry = get_object_or_404(DiaryEntry, pk=id)
    context = {'entry': entry}
    return render(request, "entrydetail.html", context)
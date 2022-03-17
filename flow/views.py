from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponseRedirect

from flow.forms import DocumentForm

# Create your views here.
def index(request):
    return render(request, 'flow/index.html')


def file_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.files.values)
            form.save()
            form = DocumentForm()
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'flow/form.html', {'form': form})    
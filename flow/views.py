from django.shortcuts import get_object_or_404, redirect, render

from flow.forms import DocumentForm, EditDocument
from flow.models import Document
from flow.helpers.utils import check_type, check_file, save_doc_file

# Create your views here.
def index(request):
    docs = Document.objects.all()
    return render(request, 'flow/index.html', {'docs': docs})

def document_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    doc_url = document.document.url
    data_sufix = check_type(doc_url)
    datas = check_file(data_sufix, doc_url)

    # assign row
    row = []
    if data_sufix == ".csv":
        row = datas[0]
        datas = datas[1:]
    return render(request, 'flow/document_view.html', {'document': document, "data_sufix": data_sufix, "datas": datas, "row": row})


def file_upload(request):
    if request.method == 'POST':    
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            print(form.files.values)
            form.save()
            form = DocumentForm('')
            return redirect('index')
    else:
        form = DocumentForm()
    return render(request, 'flow/form.html', {'form': form})    

def edit_view(request, pk):
    document = get_object_or_404(Document, pk=pk)
    doc_url = document.document.url
    data_sufix = check_type(doc_url)
    datas = check_file(data_sufix, doc_url)

    if request.method == 'POST':
        form = EditDocument(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            gender = form.cleaned_data['gender']
            ip_address = form.cleaned_data['ip_address']
            id = len(datas)
            

            data = [
                id, first_name, last_name, email, gender, ip_address
            ]

            save_doc_file(data_sufix, doc_url, data)

            form.save()

            return redirect('document_view', pk=pk )
    else:
        form = EditDocument()

    return render(request, 'flow/edit.html', {"document": document, "form": form, "datas": datas}) 
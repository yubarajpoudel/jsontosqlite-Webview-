from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from jsonsqlite.converter import createTableWith, insertDataInTable
from .forms import DocumentForm
from .models import Document
import json

def simple_upload(request):
    if request.method == 'POST' and request.FILES['d']:
        tables = request.FILES['t']
        datas = request.FILES['d']
        fs = FileSystemStorage()
        tablesName = fs.save(tables.name, tables)
        datasName = fs.save(datas.name, datas)

        if(fs.exists("mydb")):
            fs.delete("mydb")

        with open(fs.path(tablesName), "r") as inputTableJSON:
            for table in json.load(inputTableJSON):
                createTableWith(table['name'], table['schemas'], fs.base_location+"/mydb")

        if fs.exists('mydb'):
            fs.delete(tablesName)

        with open(fs.path(datasName), "r") as inputJSON:
            data = inputJSON.read()

        insertDataInTable(data, fs.path('mydb'))
        fs.delete(datasName)
        uploaded_file_url = fs.url('mydb')
        return render(request, 'jsonsqlite/simple_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'jsonsqlite/simple_upload.html')

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DocumentForm()
    return render(request, 'jsonsqlite/model_form_upload.html', {
        'form': form
    })

def home(request):
    documents = Document.objects.all()
    return render(request, 'jsonsqlite/home.html', { 'documents': documents })

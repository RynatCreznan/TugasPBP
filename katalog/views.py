from django.shortcuts import render
from katalog.models import CatalogItem

def show_katalog(request):
    data_catalog_item = CatalogItem.objects.all()
    context = {
    'name': 'Elang Permana',
    'student_id': '2006520405',
    'list_katalog': data_catalog_item
    }
    return render(request, 'katalog.html',context)
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import JsonResponse

from core.models import Medicines
# Create your views here.


@csrf_exempt
def main_render(request):
    return render(request, 'compiler.html')


@csrf_exempt
def medicines_all(request):
    medicines = Medicines.objects.all().values()
    medicines_list = list(medicines)

    return JsonResponse(medicines_list, safe=False)


@csrf_exempt
def medicines(request, med_name):
    medicines = Medicines.objects.filter(name__icontains=med_name.upper()).values()
    medicines_list = list(medicines)

    return JsonResponse(medicines_list, safe=False)


@csrf_exempt
def medicines_specify(request, med_name, value):
    medicines = Medicines.objects.filter(name__icontains=med_name.upper()).values(value)
    medicines_list = list(medicines)

    return JsonResponse(medicines_list, safe=False)

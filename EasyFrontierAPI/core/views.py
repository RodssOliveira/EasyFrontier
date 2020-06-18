from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse, JsonResponse

import datetime, json

from core.models import Medicines, Order
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

@csrf_exempt
def order_process(request):

    medicines = Medicines.objects.filter(type__status='Remédio').order_by('name')
    hygienic = Medicines.objects.filter(type__status='Higiene Pessoal').order_by('name')
    cosmetics = Medicines.objects.filter(type__status='Cosméticos').order_by('name')

    dic = {'medicine': medicines, 'hygienic': hygienic, 'cosmetics': cosmetics}

    return render(request, 'order.html', dic)

@csrf_exempt
def code_generator(request):
    if request.method == 'POST':
        products = request.POST.getlist('cart[]')
        now = datetime.datetime.now()

        code = ""
        order_num = Order.objects.all().values('code').last()
        if len(products) > 1:
            code = '#DIV' + str(order_num['code']) + '/' + str(now.year)
            code_number = int(order_num['code']) + 1
            code_string = f"{code_number:06d}"
            Order.objects.create(code=code_string)

        else:
            type = Medicines.objects.filter(name=products[0]).values('type')
            if type[0]['type'] == 1:
                code = '#REM' + str(order_num['code']) + '/' + str(now.year)
            elif type[0]['type'] == 2:
                code = '#COM' + str(order_num['code']) + '/' + str(now.year)
            elif type[0]['type'] == 3:
                code = '#HIG' + str(order_num['code']) + '/' + str(now.year)

            code_number = int(order_num['code']) + 1
            code_string = f"{code_number:06d}"
            Order.objects.create(code=code_string)

        data = json.dumps(code)

        return HttpResponse(data, content_type='applications/json')

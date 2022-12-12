from django.shortcuts import render, redirect
from django.http import JsonResponse,HttpResponse
import json
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from home import models
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], email=request.POST['email'], is_active=False)
            auth.login(request, user)
            return render(request, 'signup_waiting.html', {'user':user})
        return redirect('/')
    return render(request, 'signup.html')

# @login_required
def welcome_home(request):      # return HttpResponse("HttpResponse : /home/templates/welcome_home.html.")
	return render(request, 'welcome_home.html')

#################################################################################################################################################

################################################ 반품 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def tbList(request):
    try:
        res = models.now_tb()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)

################################################ 상품 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def pro_ins(request):
    if (request.method == 'POST'):
        print('test')
        
        data = json.loads(request.body)
        code = data["product_code"]
        name = data["product_name"]
        brand = data["product_brand_name"]
        price = data["product_price"]
        stock = data["product_stock"]
    
        try:
            query = (code, name, brand, price, stock)
            res = models.insert_prod(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)

################################################ 재무 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def finance(request):
    try:
        res = models.fin_manage()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 재무 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def pros_manage(request):
    try:
        res = models.proS_manage()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 상품 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def pro_view(request):
    try:
        res = models.pro_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 입출고 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def proS_view(request):
    try:
        res = models.proS_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 발주 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def sales_view(request):
    try:
        res = models.SALES_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 직원 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def staff_view(request):
    try:
        res = models.staff_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 고객 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def clients_view(request):
    try:
        res = models.clients_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 브랜드 현황 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def brand_view(request):
    try:
        res = models.brand_view()
        # print(res)
        return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
    except: return JsonResponse({'message':'DB_ERR'},status=400)
    
################################################ 입출고 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def proS_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        code = data["pro_code"]
        Pstat = data["pro_Stat"]
        Psum = data["pro_sum"]
        
        try:
            query = (code, Pstat, Psum)
            res = models.insert_prod_s(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 반품 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def tb_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        code = data["tb_code"]
        name = data["tb_name"]
        stock = data["tb_stock"]
        tbstat = data["tb_stat"]
        
        try:
            query = (code, name, stock, tbstat)
            res = models.insert_tb(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 수수료 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def comm_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        bname = data["br_name"]
        bcomm = data["br_comm"]
        pcomm = data["pr_comm"]

        try:
            query = (bname, bcomm, pcomm)
            res = models.insert_comm(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 브랜드 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def br_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        name = data["brand_name"]
        num = data["brand_kind_num"]
        acc = data["brand_account"]
        tel = data["brand_tel"]

        try:
            query = (name, num, acc, tel)
            res = models.insert_br(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 직원 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def staff_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        char = data["charge_br"]
        pay = data["Sta_pay"]
        att = data["Sta_Att"]
        name = data["Sta_name"]

        try:
            query = (char, pay, att, name)
            res = models.insert_staff(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 고객 추가 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def client_ins(request):
    if (request.method == 'POST'):
        
        data = json.loads(request.body)
        
        num = data["clients_num"]
        name = data["clients_name"]
        add = data["clients_add"]
        tel = data["clients_tel"]
        note = data["clients_note"]

        try:
            query = (num, name, add, tel, note)
            res = models.insert_client(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 상품 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_prod(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        code = data["product_code"]

        try:
            query = (code)
            res = models.del_prod(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 반품 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_tb(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        code = data["tb_code"]

        try:
            query = (code)
            res = models.del_tb(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 브랜드 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_brand(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        name = data["brand_name"]

        try:
            query = (name)
            res = models.del_brand(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 발주 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_sales(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        num = data["pro_num"]

        try:
            query = (num)
            res = models.del_sales(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 인사 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_staff(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        name = data["charge_br"]

        try:
            query = (name)
            res = models.del_staff(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
        
################################################ 고객 삭제 ##################################################

@method_decorator(csrf_exempt,name='dispatch')
def del_client(request):
    if (request.method == 'DELETE'):
        
        data = json.loads(request.body)
        
        num = data["clients_num"]

        try:
            query = (num)
            res = models.del_client(query)
            # res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)
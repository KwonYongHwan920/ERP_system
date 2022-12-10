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
        
        data = json.loads(request.body)
        
        code = data["product_code"]
        name = data["product_name"]
        brand = data["product_brand_name"]
        price = data["product_price"]
        stock = data["product_stock"]
    
        try:
            query = (code, name, brand, price, stock)
            models.insert_prod(query)
            res = models.pro_view()
            return JsonResponse({'message': 'SUCCESS','res':res}, status=200)
        except: return JsonResponse({'message':'DB_ERR'},status=400)

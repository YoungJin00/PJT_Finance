from django.shortcuts import render
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
import requests
from .models import DepositProducts, DepositOptions
from .serializers import DepositOptionsSerializer, DepositProductsSerializer


BASE_URL = 'http://finlife.fss.or.kr/finlifeapi/'

@api_view(['GET'])
def api_test(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()
    return JsonResponse({'response': response})

@api_view(['GET'])
def save_deposit_products(request):
    URL = BASE_URL + 'depositProductsSearch.json'
    params = {
        'auth' : settings.API_KEY,
        'topFinGrpNo': '020000',
        'pageNo': 1
    }
    response = requests.get(URL, params=params).json()

    for li in response.get('result').get('baseList'):
        if not DepositProducts.objects.filter(fin_prdt_cd=li.get('fin_prdt_cd')).exists():
            serializer = DepositProductsSerializer(data = li)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    for li in response.get('result').get('optionList'):
        product = DepositProducts.objects.get(fin_prdt_cd = li.get('fin_prdt_cd'))
        serializer = DepositOptionsSerializer(data=li)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product=product)

    return JsonResponse({'message': 'okay'})

        

@api_view(['GET', 'POST'])
def deposit_products(request):
    if request.method == "GET":
        product = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(product, many= True)
        return Response(serializer.data)
    else:
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)

    

@api_view(['GET'])
def deposit_products_options(request, fin_prdt_cd):    
    product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
    options = DepositOptions.objects.filter(product=product)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def top_rate(request):
    options = DepositOptions.objects.order_by('-intr_rate2').first()
    product = DepositProducts.objects.get(pk=options.product.pk)
    opserializer = DepositOptionsSerializer(options)
    proserializer = DepositProductsSerializer(product)
    result = {
        'deposit_product': proserializer.data,
        'options': opserializer.data
    }

    return Response(result)
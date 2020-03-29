from django.shortcuts import render
from django.http.response import HttpResponse, JsonResponse
from django.http.request import HttpRequest
from api.models import Product, Category


# Create your views here.

def product_list(response):
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_details(response, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(product.to_json())


def category_list(response):
    categories = Category.objects.all()
    categories_json = [category.to_json() for category in categories]
    return JsonResponse(categories_json, safe=False)


def category_details(response, category_id):
    try:
        category = Category.objects.get(id=category_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'error': str(e)})
    return JsonResponse(category.to_json())


def category_products(response, id):
    products = Product.objects.filter(category_id=id)
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)

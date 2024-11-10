from django import template
from shop.models import ProductModel,ProductStatusType

register = template.Library()

@register.inclusion_tag("includes/latest-products.html")
def show_latest_products():
    latest_products = ProductModel.objects.filter(status=ProductStatusType.active.value).order_by('-created_date')[:8]
    return {"latest_products":latest_products}

@register.inclusion_tag("includes/similar-products.html")
def show_similar_products(product):
    product_category = product.category.all()
    similar_products = ProductModel.objects.filter(status=ProductStatusType.active.value,category__in=product_category).order_by('-created_date')[:4]
    return {"similar_products":similar_products}
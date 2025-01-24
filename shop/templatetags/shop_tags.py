from django import template
from shop.models import ProductModel,ProductStatusType,WishListModel

register = template.Library()

@register.inclusion_tag("includes/latest-products.html",takes_context=True)
def show_latest_products(context):
    request = context.get("request")
    latest_products = ProductModel.objects.filter(
        status=ProductStatusType.active.value).distinct().order_by("-created_date")[:8]
    wishlist_items = WishListModel.objects.filter(user=request.user).values_list("product__id",flat=True) if request.user.is_authenticated else []
    return {"latest_products": latest_products,"request":request,"wishlist_items":wishlist_items}


@register.inclusion_tag("includes/similar-products.html", takes_context=True)
def show_similar_products(context, product):
    request = context.get("request")
    if not product:
        return {"similar_products": [], "request": request, "wishlist_items": []}
    
    product_category = product.category.all()
    similar_products = ProductModel.objects.filter(
        status=ProductStatusType.active.value,
        category__in=product_category
    ).distinct().exclude(id=product.id).order_by("-created_date")[:4]
    
    wishlist_items = WishListModel.objects.filter(user=request.user).values_list("product__id", flat=True) if request.user.is_authenticated else []
    return {
        "similar_products": similar_products,
        "request": request,
        "wishlist_items": wishlist_items
    }



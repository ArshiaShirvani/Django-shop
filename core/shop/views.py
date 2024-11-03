from django.shortcuts import render
from django.views.generic import (TemplateView,
                                  ListView,
                                  DetailView)
from .models import (ProductModel,
                     ProductCategoryModel,
                     ProductStatusType)


class ProductListView(ListView):
    template_name = 'shop/product-grid.html'
    queryset = ProductModel.objects.filter(status=ProductStatusType.active.value)

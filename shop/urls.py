from django.urls import path
from .views import *



app_name = 'shop'


urlpatterns = [
    path('', product_in_category, name='product_all'),
    path('categories/<slug:category_slug>/', product_in_category, name='product_in_category'),
    path('mypage/<int/pk>/', product_mypage, name='product_mypage'),
    path('<int:pk>/<product_slug>/', ProductDetailView.as_view(), name='product_detail'),
#    path('upload/', ProductUploadView.as_view(), name='product_upload'),
    path('search/', search, name='search'),
    path('delete/<int:pk>/<product_slug>/', ProductDeleteView.as_view(), name='product_delete'),
    path('update/<int:pk>/<product_slug>/', ProductUpdatedView.as_view(), name='product_update'),
]
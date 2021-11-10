from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('services/',views.service,name='services'),
    path('products/', views.products,name='products'),
    path('partners/', views.partners,name='partners'),
    path('contact/', views.contact,name='contact'),
    path('blog/',views.PostList.as_view(),name = 'blog'),
    path('<slug:slug>/',views.PostDetail.as_view(),name = "post_detail"),
]
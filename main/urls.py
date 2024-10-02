from django.urls import path

from .views import HomePageView, ShopPageView, ServicesView, ContactPageView, SingleProductView, AboutPageView, CategoryView, Product


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('shop/', ShopPageView.as_view(), name="shop"),
    path('services/', ServicesView.as_view(), name="services"),
    path('contact/', ContactPageView.as_view(), name="contact"),
    path('single/<str:product_slug>', SingleProductView.as_view(), name="single"),
    path('about/', AboutPageView.as_view(), name="about"),
    path('category/<int:category_id>', CategoryView.as_view(), name="category"),
    path('search/', HomePageView.as_view(), name="search")
]
    
from django.urls import path
from . import views
from custom_loggin import views as loggin_views





urlpatterns = [
    #adding product url
    path('add/', views.add_product, name='add_product'),

    #home page that shows all products
    path('', views.product_list, name='product_list'),

    #product details (after clicking on product list iteams views each iteam info)+rates
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),
    path('product_detail/<int:pk>/add_review/', views.add_review, name='add_review'),  # Define the URL pattern for adding a review


    #user dashboard page (include user info - shopping info - & ...)
    path('dashboard/', loggin_views.dashboard, name='dashboard'),
    
    #website about page that shows seller info and ways for comunication
    #path('about/', views.about, name='about'),
    
    #category page
    path('category/<str:foo>', views.category, name='category'),

    #category summary
    path('category_summary/', views.category_summary, name="category_summary"),

    #search
    path('search/', views.search_view, name="search"),
    path('detail/<int:pk>/', views.detail_view, name='detail'),  
    
    #all products with filter option
    path('all_products', views.all_products, name='all_products'),  
    
    #filter Products 
    path('Discounted/', views.Discounted, name='Discounted'),
    path('CategoryFilter/', views.filter_by_category, name='filter_by_category'),

    #bestSELLER
    path('best-selling-product/', views.best_selling_product, name='best_selling_product'),




]
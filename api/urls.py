from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet, ReviewViewSet, OrderViewSet, MyUserViewSet, CartViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'carts', CartViewSet)

router.register(r'users', MyUserViewSet)

urlpatterns = router.urls

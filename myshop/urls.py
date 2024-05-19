from django.contrib import admin
from django.urls import path, include
from payment import urls as payments_urls
#adding media url 
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_swagger.views import get_swagger_view



schema_view = get_swagger_view(title='Your Project API')



urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('custom_loggin.urls')),
    path('payments/', include(payments_urls)),
    path('', include('products.urls')),
    path('cart/', include('cart.urls')),
    path('api/', include('api.urls')),
    path('api/docs/', schema_view), 


]


urlpatterns += static(settings.STATIC_URL , document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

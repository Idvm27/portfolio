from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin  # Импортируем admin правильно

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio_app.urls')),  # Подключаем ваше приложение
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

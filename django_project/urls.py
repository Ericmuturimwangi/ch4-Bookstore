from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')), 
    path('login/', LoginView.as_view(), name='login'),
    path('', include('pages.urls')),
    path("books/", include ("books.urls")),
    path ('books/', include ("books.urls")),
]+ static(
    settings.MEDIA_URL, document_root = settings.MEDIA_ROOT
)

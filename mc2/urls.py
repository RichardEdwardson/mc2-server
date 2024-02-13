"""
URL configuration for mc2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
# from api.admin import admin_site
from django.urls import path, include
from django.conf.urls.static import static

# Static file serving for development.
# See: https://docs.djangoproject.com/en/2.1/howto/static-files/#serving-files-uploaded-by-a-user-during-development
# Or: https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
# For production, use Apache or whatever, just not this. Have to look into that sometimes.
# See: https://docs.djangoproject.com/en/5.0/howto/static-files/deployment/
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('admin/', admin_site.urls),
    path('api/', include('api.urls')),
    path('chat/', include('chat.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

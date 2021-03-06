"""Aplikacja_Licencjat URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from pages_app.views import home_view
from accounts_app.views import login_view
from pages_app.views import plots_page_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('', home_view, name='home'),
    path('', include('accounts_app.urls', namespace='accounts_app')),
    path('logout/', auth_views.LogoutView.as_view(template_name=''), name="logout"),
    path('', include('pages_app.urls', namespace='pages_app')),
    path('', plots_page_view, name='plots'),
    path('plotsh/', plots_page_view),
]

#path('plts/', views.Products.getSNSData),



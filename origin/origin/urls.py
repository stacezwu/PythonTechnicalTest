"""origin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
# from django.urls import include
# from .router import router

# from bond import views
from bonds import views as view
from rest_framework.authtoken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', HelloWorld.as_view()),
    path('', view.get_bond, name='get-bond'),
    path('get-bond', view.get_bond, name='get-bond'),
    path('post-bond', view.post_bond, name='post-bond'),
    # path('filter-bond', view.filter_bond, name='filter-bond'),
    # path('api/', include(router.urls)), 
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth')
]

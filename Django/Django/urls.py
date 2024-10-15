"""
URL configuration for UrbanDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# ======= task_19-1 ===================
#
# from django.contrib import admin
# from django.urls import path
# from task1.views import games, main, reg_page_django, reg_page_html
# from django.views.generic import TemplateView
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main),
#     path('games/',games),
#     path('cart/', TemplateView.as_view(template_name='cart.html')),
#     path('reg_page_django/', reg_page_django),
#     path('reg_page_html/', reg_page_html),
#
# ]

# ======= task_19-2 ===================

#
# from django.contrib import admin
# from django.urls import path
# from task1.views import games, main, reg_page_django, reg_page_html
# from django.views.generic import TemplateView
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', main),
#     path('games/',games),
#     path('cart/', TemplateView.as_view(template_name='cart.html')),
#     path('reg_page_django/', reg_page_django),
#     path('reg_page_html/', reg_page_html),
#
# ]


# ======= task_19-5 ===================


from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),

]

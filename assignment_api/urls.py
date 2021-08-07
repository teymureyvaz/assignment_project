"""assignment_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import PostCreateView,PostStatisticsByPostIdView,PostStatisticsByUserIdView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/store', PostCreateView.as_view(), name='store'),
    path('post/statistics_by_post_id/<int:post_id>', PostStatisticsByPostIdView.as_view(), name="statistics_by_post_id"),
    path('post/statistics_by_user_id/<int:user_id>', PostStatisticsByUserIdView.as_view(),
         name="statistics_by_user_id"),

]

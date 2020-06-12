# -*- coding: utf-8 -*-
# @Time     :2020/06/06  14:59
# @Author   :qingjia
# @Email   :834789582@qq.com
# @File     urls.py
from django.urls import path
from projects   import views

urlpatterns = [
    path('index/', views.index),
    # 类视图路由的方法
    path('projects/',views.ProjectsList.as_view()),
    path('projects/<int:pk>',views.ProjectDetails.as_view())
    # 左边为转换器，右边为参数别名啥
    # path('<int:pk>/',views.Projects.as_view())
]
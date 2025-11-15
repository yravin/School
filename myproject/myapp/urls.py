from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    path("stusent/", views.student, name='student'),

    path("schedule/",views.schedule,name='schedule'),

    path('teacher/', views.teacher_list, name='teacher_list'),

    path('classgood/',views.classgood,name='classgood'),

    path('base/',views.base,name='base'),

    path('adminSythem/',views.adminmanagermentSythem,name='adminmanagermentSythem'),

    path("user/",views.User,name="User"),

    path('Score/',views.score,name='score'),

    path('admin-api/login/', views.admin_login_api, name='admin_login_api'),
]

from django.urls import path, include
from . import views

app_name='blog'

urlpatterns = [
    path('test1/', views.test1),
    path('test2/<int:id>/', views.test2),
    path('test3/<year>/<month>/<day>/', views.test3),
    path('',views.list,name='list'),
    path('<int:id>/',views.detail,name='detail'),
    path('test4/',views.test4),
    path('profile/',views.profile),
    path('tag/<id>',views.tag_list),
    path('test7/',views.test7),
    path('new/',views.post_create,name='create'),
    path('update/<id>/',views.post_update,name='update'),
    path('delete/<id>/',views.post_delete,name='delete'),
]

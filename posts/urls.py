from django.urls import URLPattern, path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [
    path('',views.Index, name='index'),
    path('delete/<int:post_id>/',views.delete,name='delete'),
    path('edit/<int:post_id>/',views.edit,name='edit'),
    path('like/<int:post_id>/',views.like,name='likes'),

]
from django.urls import path
from . import views
urlpatterns=[
    path('abc',views.index),
    path('def',views.index2),
    path('ghi',views.index3),
    path('jkl',views.index4),
    path('hello',views.abc)
]
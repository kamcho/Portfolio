
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


from django.urls import path
from .views import Home


urlpatterns=[

    path('',Home.as_view(),name='home'),

    # path('',ContactView.as_view(),name='contactus'),
]
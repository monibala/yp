from django.urls import path
from . import views 
urlpatterns =[ 
    path('blog/', views.blog, name='blog'),
    path('blogdetail/<int:id>', views.blogdetail, name='blogdetail'),
    path('search/',views.search, name='search'),
]
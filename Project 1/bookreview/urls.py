from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('books/', include('books.urls'))
    path('authors/', views.AuthorView.as_view(),name='author-list'),
    path('authors/<int:pk>', views.AuthorInstanceView.as_view(),name='author-instance'),
    path('', views.index_view, name='index')
]
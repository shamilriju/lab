from django.urls import path

from lab import views

urlpatterns=[
    path("",views.main,name='main'),
    path('bookingss/<int:id>',views.bookingss,name='bookingss'),
    path('booking',views.booking,name='booking'),
    path('mybooking',views.mybooking,name='mybooking'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
]
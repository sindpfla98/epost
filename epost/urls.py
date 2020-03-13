from django.urls import path
from django.conf.urls import url, include
from epost import views

app_name = 'epost'

urlpatterns = [
    path('search', views.Search.as_view(), name='search'),
    path('listing', views.Listing.as_view(), name='listing'),
    path('listing_search', views.listing_search)
]

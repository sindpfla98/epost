from django.urls import path
from django.conf.urls import url, include
from epost import views

app_name = 'epost'

urlpatterns = [
    path('keyword', views.Keyword.as_view(), name='keyword'),
    path('keyword_search', views.keyword_search, name='keyword_search'),
    path('listing', views.Listing.as_view(), name='listing'),
    path('listing_search', views.listing_search, name='listing_search')
]

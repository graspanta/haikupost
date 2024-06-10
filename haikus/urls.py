from django.urls import path
from .views import HaikuListView, HaikuDetailView, HaikuCreateView, SearchResultsListView

urlpatterns = [
    path('create/', HaikuCreateView.as_view(), name='haiku_create'),
    path('<uuid:pk>/', HaikuDetailView.as_view(), name='haiku_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
    path('', HaikuListView.as_view(), name='haiku_list'),
]
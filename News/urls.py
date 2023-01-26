from django.urls import path
from News.views import NewsList, NewsDetail



urlpatterns = (
    path('', NewsList.as_view(),name='news'),
    path('<int:pk>/',NewsDetail.as_view(),name='news_detail' ),
)
from django.urls import path
from Ads.views import AdsListView,DetailAd,AdCreateView,AdApdateView,AdDeleteView,Comments, Gamelist,  updateCommentActive


urlpatterns = [
    path('',AdsListView.as_view(),name='ads'),
    path('<int:pk>/',DetailAd.as_view(),name='ad_detail'),
    path('create/',AdCreateView.as_view(), name='ad_cteate'),
    path('<int:pk>/update/', AdApdateView.as_view(), name='ad_update'),
    path('<int:pk>/delete/', AdDeleteView.as_view(), name='ad_delete'),
    path('comments/',Comments.as_view(), name='comments'),
    path('game/<str:game>/',Gamelist,name='game'),
    path('update_comment_active/<int:pk><slug:type>', updateCommentActive, name='update_comment_active'),
    
]
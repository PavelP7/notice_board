from django.urls import path
from .views import NoticeCreate, NoticeList, NoticeDetail, Dashboard

urlpatterns = [
    path('', NoticeList.as_view(), name='notice_list'),
    path('<int:pk>/', NoticeDetail.as_view(), name='notice_detail'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('notice_create/', NoticeCreate.as_view(), name='notice_create'),
]

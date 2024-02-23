from django.urls import path
from . import views

app_name = 'polls'

urlpatterns = [
#    path('', views.IndexView.as_view(), name='index'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

#    path('create/', views.CreateView.as_view(), name='create'),
#    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
#    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'),
]
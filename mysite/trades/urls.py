from django.urls import path

from . import views

app_name = 'trades' # Add a namespace
# urlpatterns = [
#     # ex: /polls/
#     path('', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]
urlpatterns = [
    path('', views.index, name='index'),
    #path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    ###path('add/', views.ResultsView.as_view(), name='add'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
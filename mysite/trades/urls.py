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
    path('daily/', views.DailyView.as_view(), name='daily'),
    path('add/', views.add, name='add'),
    # path('daily/', views.daily, name='daily'),
    path('<int:pk>/delete/', views.TradeDelete.as_view(), name='delete'),
    path('<int:trade_id>/edit/', views.edit, name='edit'),
    path('archive/', views.archive, name='archive'),
    path('settings/', views.settings, name='settings'),
    path('render/pdf/', views.Pdf.as_view(), name='report'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]

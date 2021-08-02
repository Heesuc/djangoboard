from django.urls import path
from django.conf.urls import include

from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('board', views.board, name='board'),
    path('board_write', views.board_write, name='board_write'),
    path('board_insert', views.board_insert, name='board_insert'),
    path('board_view', views.board_view, name='board_view'),
    path('board_delete', views.board_delete, name='board_delete'),
    path('board_update', views.board_update, name='board_update'),
    path('board_edit', views.board_edit, name='board_edit'),

    #REST API
    #path('/', views.index, name='index'),
    #path('viewjson', views.viewjson, name='board_edit'),
]

from django.urls import path

from configuration import views

app_name = 'configuration'

handler404 = 'core.views.page_not_found'
handler500 = 'core.views.server_error'
handler403 = 'core.views.permission_denied'

urlpatterns = [
    path('gym/136/', views.anagrafica_detail, name='anagrafica_detail'),
    path('gym/136/edit/', views.anagrafica_edit, name='anagrafica_edit'),
    path('lesson/create/', views.lesson_create, name='lesson_create'),
    path('lesson/', views.lessons, name='lessons'),
    path('lesson/<int:post_id>/', views.lesson_detail, name='lesson_detail'),
    path('lesson/<int:post_id>/edit/', views.lesson_edit, name='lesson_edit'),
    path('lesson/<int:post_id>/delete/',
         views.lesson_delete,
         name='lesson_delete'),
    path('trainer/create/', views.trainer_create, name='trainer_create'),
    path('trainer', views.trainers, name='trainers'),
    path('trainer/<int:post_id>/',
         views.trainer_detail,
         name='trainer_detail'),
    path('trainer/<int:post_id>/edit/',
         views.trainer_edit,
         name='trainer_edit'),
    path('pricelist/create/',
         views.pricelist_create,
         name='pricelist_create'),
    path('pricelist', views.pricelists, name='pricelists'),
    path('pricelist/<int:post_id>/',
         views.pricelist_detail,
         name='pricelist_detail'),
    path('pricelist/<int:post_id>/edit/',
         views.pricelist_edit,
         name='pricelist_edit'),
]

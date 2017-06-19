from django.conf.urls import url

from . import views

urlpatterns = [
    #url(r'^$', views.get_name, name='name')
    url(r'^$', views.index, name='index'),
    url(r'callbacks', views.callbacks, name='callbacks'),
    url(r'user_form',views.user_form,name='user_form')

    #url(r'^action', views.get_name, name="action")
]
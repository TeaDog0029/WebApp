from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.welcome_view, name = 'welcome_view'),
	url(r'^add/$', views.add_tint, name = 'add_tint'),
	url(r'^details/(?P<pk>\d+)/$', views.details, name = 'details'),
	url(r'^ranking/$', views.tint_list, name = 'ranking')
]
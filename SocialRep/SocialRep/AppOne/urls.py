from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'tweets',views.TweetViewSet)

urlpatterns = [
	url(r'^$', views.liveFeed, name = 'liveFeed'),
	url(r'^api-tweet$',include('rest_framework.urls', namespace = 'rest_framework')),
]
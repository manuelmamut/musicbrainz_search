from django.conf.urls import url
from django.views.generic import RedirectView
from search import views



urlpatterns = [
    url(r'^$', RedirectView.as_view(url='release-groups/')),
    url(r'^release-groups/$', views.releaseGroupView.as_view(), name='release-groups'),
]

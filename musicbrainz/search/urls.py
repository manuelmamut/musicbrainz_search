from django.conf.urls import url
from django.views.generic import RedirectView
from search import views
from django.views.decorators.cache import cache_page



urlpatterns = [
    url(r'^$', RedirectView.as_view(url='release-groups/')),
    url(r'^release-groups/$', cache_page(60 * 15)(views.releaseGroupView.as_view()), name='release-groups'),
    url(r'^release-groups-nocache/$', views.releaseGroupView.as_view(), name='release-groups-nocache'),
]

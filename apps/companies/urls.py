from django.conf.urls import url

from .api.v1 import views as api_v1_views

app_name = 'companies'

urlpatterns = [
    url(
        r'^api/v1/companies/$',
        api_v1_views.CompanyListAPIView.as_view(),
        name='list',
    ),
    url(
        r'^api/v1/companies/(?P<pk>\d+)/$',
        api_v1_views.CompanyRetrieveUpdateAPIView.as_view(),
        name='detail',
    ),
]
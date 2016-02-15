from django.conf.urls import include, url

from gems import views as gem_views
from gems import urls as gem_urls

urlpatterns = [
    url(r'^$', gem_views.home_page, name='home'),
    url(r'^lists/', include(gem_urls)),
    # url(r'^admin/', include(admin.site.urls)),
]


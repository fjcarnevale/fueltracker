from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'fueltracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^mpg/', include('mpg.urls')),
    url(r'^admin/', include(admin.site.urls)),
]

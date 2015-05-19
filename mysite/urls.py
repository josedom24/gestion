from django.conf.urls import patterns, include, url
from django.contrib import admin

from mysite.views import Index

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^centro/', include('centro.urls')),
    url(r'^convivencia/', include('convivencia.urls')),
    url(r'^registro/', include('registro.urls')),
    url(r'^impresora/', include('impresora.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    (r'^tinymce/', include('tinymce.urls')),
)




from django.contrib import admin
from django.conf.urls import *
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'portfolio.views.index', name='index'),
    url(r'^inicial/', 'portfolio.views.index', name='index'),
    url(r'^contato/', 'portfolio.views.contato', name='contato'),
    url(r'^contato/enviacontato/', 'portfolio.views.enviacontato', name='enviacontato'),
    url(r'^sobre/', 'portfolio.views.sobre', name='sobre'),
    url(r'^portfolio/', 'portfolio.views.portfolio', name='portfolio'),
    url(r'^job/(?P<nr_item>[a-zA-Z0-9_.-]+)/$','portfolio.views.job'),
    # url(r'^cristian/', include('cristian.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
    url(r'^redactor/', include('redactor.urls')),
    url(r'^ajaximage/', include('ajaximage.urls')),


    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$','django.views.static.serve', {'document_root':settings.MEDIA_ROOT}),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
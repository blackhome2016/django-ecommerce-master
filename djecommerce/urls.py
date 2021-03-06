from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls.i18n import i18n_patterns




urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', include('core.urls', namespace='core')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)

#urlpatterns = [
#    path('admin/', admin.site.urls),

#]
#urlpatterns += i18n_patterns(
#    path('accounts/', include('allauth.urls')),
#    path('', include('core.urls', namespace='core')),
#    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
#    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
#    prefix_default_language=False,
#
#)

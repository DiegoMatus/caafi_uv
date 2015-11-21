from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = 'CAAFI'
urlpatterns = patterns('apps.caafi.views',
    url(r'^$', 'index', 	name='index'),
    url(r'^(?P<language_slug>\w+)/(?P<category_slug>[\w|\W]+)/(?P<subcategory_slug>[\w|\W]+)/$',	'urls_view', 		name='urls'),
    url(r'^(?P<language_slug>\w+)/(?P<category_slug>[\w|\W]+)/$', 							'subcategories_view',		name='subcategories'),
    url(r'^(?P<language_slug>\w+)/$', 														'categories_view',			name='categories'),
    url(r'^url/add', 																		'reported_urls_view',		name='reported_urls'),
) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 	#Servir estáticos en desarrollo
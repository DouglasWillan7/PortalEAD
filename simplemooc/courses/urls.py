from django.conf.urls import url, patterns, include

urlpatterns = patterns('simplemooc.courses.views',
                       url(r'^$', 'index', name='index'),

                       )


from django.conf.urls import url, patterns, include

urlpatterns = patterns('simplemooc.core.views',
                       url(r'^$', 'home', name='home'),
                       url(r'^contato/$', 'contact', name='contact')
                       )


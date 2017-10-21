import os
from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^$', 'django.views.generic.base.TemplateView', {'template': 'dashboard.html'}),
    (r'^search/$', 'django.views.generic.Template', {'template': 'search.html'}),
    
    (r'^accounts/login/$', "malnutrition.ui.views.login.login"),    
    (r'^logout/$', "malnutrition.ui.views.login.logout"),

    (r'^static/webui/(?P<path>.*)$', "django.views.static.serve", {"document_root": os.path.dirname(__file__) + "/static"})
)
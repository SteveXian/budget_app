from django.conf.urls import patterns, include, url
from budgetTool import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'budgetTool.views.home', name='home'),
    # url(r'^budgetTool/', include('budgetTool.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'budget.views.index'),
    url(r'^login/$', 'budget.views.user_login'),
    url(r'^logout/$', 'budget.views.user_logout'),
    url(r'^login_auth/$', 'budget.views.login_auth'),
    url(r'^new_user/$', 'budget.views.new_user'),
    url(r'^check_username$', 'budget.views.check_username'),
    url(r'^create_user/$', 'budget.views.create_user'),
    url(r'^logout/$', 'budget.views.user_logout'),

    url(r'^user/update/$', 'budget.views.user_update'),
    url(r'^user/edit/$', 'budget.views.user_edit'),

    url(r'^planning/$', 'budget.views.user'),
    url(r'^planning/update/$', 'budget.views.planning_update'),
    url(r'^tracking/$', 'budget.views.tracking'),
    url(r'^tracking/add/$', 'budget.views.tracking_add'),
    url(r'^tracking/delete/(\d*)$', 'budget.views.tracking_delete'),
)

urlpatterns += patterns('',
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)

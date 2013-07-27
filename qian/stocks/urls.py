from django.conf.urls import patterns, url

urlpatterns = patterns('stocks.views',
    url(r'^$', 'home', name='home'),
    url(r"^categories/$", "categories"),
)

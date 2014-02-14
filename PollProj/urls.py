from django.conf.urls import patterns, include, url
from django.contrib import admin
from polls import views
from polls.api import EntryResource, UserResource, PollResource, ChoiceResource, TweetResource, TwitterUserResource
from tastypie.api import Api
from django.views.generic import TemplateView

admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(EntryResource())
v1_api.register(PollResource())
v1_api.register(ChoiceResource())
v1_api.register(TweetResource())
v1_api.register(TwitterUserResource())


urlpatterns = patterns('',

    url(r'^$', views.IndexView.as_view(), name='index'),
    # url(r'^polls/$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^polls/', include('PollProj.urls', namespace='polls')),
    url(r'^polls/(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>\d+)/vote/$', views.vote, name='vote'),
    url(r'^api/', include(v1_api.urls)),
    url(r'^polls/twmain/$', TemplateView.as_view(template_name='twitter_main.html'), name="twmain"),
    url(r'^polls/twdetail/$', TemplateView.as_view(template_name='twitter_detail.html'), name="twdetail"),
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),

)
from django.conf.urls.defaults import patterns, url, include
from project.views import Demo


urlpatterns = patterns(u"",
    url(r"^$", Demo.as_view()),
    url(r"^", include("cssreload.urls")),
)

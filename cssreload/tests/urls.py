from django.conf.urls.defaults import patterns, include, url


urlpatterns = patterns(u"",
    url(r"^testview$", "cssreload.tests.views.testview", name="testview"),
    url(r"^", include("cssreload.urls")),
)

from django.conf.urls.defaults import patterns, url


urlpatterns = patterns("cssreload.views",
    url(r"cssreload$", "cssreload", name="cssreload"),
)

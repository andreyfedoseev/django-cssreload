from django.conf import settings
from django.core.urlresolvers import reverse
from django.template.context import Context
from django.template.loader import render_to_string
from django.utils.encoding import smart_unicode
import re


try:
    STATIC_URL = settings.STATIC_URL
except AttributeError:
    STATIC_URL = settings.MEDIA_URL


class CSSReloadMiddleware(object):

    TARGET_RE = re.compile("(</\s*body\s*>)", re.I)
    VIEW_URL = reverse("cssreload")

    def process_response(self, request, response):
        if not settings.DEBUG:
            return response

        if response.status_code == 200 and response['Content-Type'].split(';')[0] == "text/html":
            widget = render_to_string("cssreload/cssreload.html",
                context_instance=Context(dict(
                    STATIC_URL=STATIC_URL,
                    VIEW_URL=self.VIEW_URL,
                ))
            )
            response.content = self.TARGET_RE.sub(
                smart_unicode(widget) + r"\1",
                smart_unicode(response.content),
                count=1
            )
            if response.get('Content-Length', None):
                response['Content-Length'] = len(response.content)

        return response

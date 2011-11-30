from django.core.urlresolvers import reverse
from django.http import HttpRequest, HttpResponse
from unittest import main, TestCase
import os


os.environ["DJANGO_SETTINGS_MODULE"] = "cssreload.tests.django_settings"


class CSSReloadTestCase(TestCase):

    def test_middleware(self):
        from cssreload.middleware import CSSReloadMiddleware

        middleware = CSSReloadMiddleware()

        html = "<html><head></head><body>TEST</body></html>"
        response = HttpResponse(html, content_type="text/html")
        response = middleware.process_response(HttpRequest(), response)
        self.assertEquals(response.content, """<html><head></head><body>TEST<link rel="stylesheet" href="/media/cssreload/cssreload.css">
<div id="django-cssreload">
  CSS Reload:
  <a href="#" class="disable">On</a>
  <a href="#" class="enable">Off</a>
</div>
<script type="text/javascript" src="/media/cssreload/cssreload.js"></script>
<script type="text/javascript">
  new django_cssreload('/media/', '/cssreload');
</script>
</body></html>""")

        from django.conf import settings
        settings.DEBUG = False
        response = HttpResponse(html, content_type="text/html")
        response = middleware.process_response(HttpRequest(), response)
        self.assertEqual(response.content, html)
        settings.DEBUG = True


        response = HttpResponse(u"Not Found", status=404)
        response = middleware.process_response(HttpRequest(), response)
        self.assertEquals(response.content, u"Not Found")

        response = HttpResponse(u'{foo:"bar"}', content_type="application/json")
        response = middleware.process_response(HttpRequest(), response)
        self.assertEquals(response.content, u'{foo:"bar"}')

    def test_view(self):
        from django.test.client import Client
        client = Client()
        view_url = reverse("cssreload")
        response = client.post(view_url, dict())
        self.assertEqual(response["Content-Type"], "application/json")
        self.assertEqual(response.content, "{}")

        test_css = os.path.join(os.path.dirname(__file__), "media", "styles", "test.css")
        mtime = os.path.getmtime(test_css)
        response = client.post(view_url, dict(s=[
          "styles/test.css",
          "other.css",
        ]))
        self.assertEquals(response.content, '{"styles/test.css": %s}' % mtime)

if __name__ == '__main__':
    main()

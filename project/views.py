from django.views.generic import TemplateView
import os


class Demo(TemplateView):

    template_name = "demo.html"

    def get_context_data(self, **kwargs):
        readme = open(os.path.join(os.path.dirname(__file__), "..", "README.rst")).read()
        return dict(readme=readme)

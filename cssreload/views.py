from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest
import json
import os


def cssreload(request):
    if request.method != "POST":
        return HttpResponseBadRequest()

    data = {}
    for stylesheet in request.POST.getlist("s"):
        path = os.path.join(settings.STATIC_ROOT, stylesheet.split('?', 1)[0].replace("/", os.sep))
        if os.path.exists(path):
            data[stylesheet] = os.path.getmtime(path)

    return HttpResponse(json.dumps(data),
                        content_type="application/json")

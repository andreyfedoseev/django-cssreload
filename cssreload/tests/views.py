try:
    from django.shortcuts import render
except ImportError:
    from django.views.generic.simple import direct_to_template as render


def testview(request):
    return render(request, "testview.html")

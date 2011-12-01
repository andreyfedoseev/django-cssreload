======================
django-cssreload
======================
django-cssreload allows to reload stylesheets on current page automagically.
It's very handy when you need to do a lot of CSS coding.

Installation
---------------------
1. Add ``'cssreload'`` to your ``INSTALLED_APPS``
2. Add ``'cssreload.middleware.CSSReloadMiddleware'`` to your ``MIDDLEWARE_CLASSES``
3. Set ``DEBUG=True``
4. Add ``url(r"^", include("cssreload.urls"))`` to your ``urlpatterns``

After that you'll have a widget to turn CSS reload on and off on every page.

Demo
-------
See demo video: http://youtu.be/ORYXttB7Nmc

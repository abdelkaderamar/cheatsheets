main_title: Django Cheatsheet
lang: python

#------------------------------------------------------------------------------
title: Get media url prefix
<a href="{% get_media_prefix %}{{ pdf_file }}">Download</a>
#------------------------------------------------------------------------------
title: Configuring media directory	
# in settings.py
MEDIA_ROOT = 'media/generated'
MEDIA_URL = 'media/'

# in site/urls.py
from django.conf.urls.static import static
urlpatterns = [
    # ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#------------------------------------------------------------------------------


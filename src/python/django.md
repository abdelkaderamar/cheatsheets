main_title: Django Cheatsheet
lang: bash

#------------------------------------------------------------------------------
title: Create a new project
django-admin startproject myproject
# create a project in the current directory
django-admin startproject myproject
# create a project in a different directory
django-admin startproject myproject project_dir
#------------------------------------------------------------------------------
title: Filter with a list
# Filter the table Exchange based on a list of MIC codes
exchanges = Exchange.objects.filter(mic_code__in=exchanges_mics)
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


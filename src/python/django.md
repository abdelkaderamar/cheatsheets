main_title: Django Cheatsheet
lang: bash

#------------------------------------------------------------------------------
#- section: The Basics
title: Create a new project
django-admin startproject myproject
# create a project in the current directory
django-admin startproject myproject .
# create a project in a different directory
django-admin startproject myproject project_dir
#------------------------------------------------------------------------------
title: Start the server
python manage.py runserver
python manage.py runserver 8080
#------------------------------------------------------------------------------
title: Create an app
python manage.py startapp app_name
#------------------------------------------------------------------------------
title: Create database table
python manage.py migrate
#------------------------------------------------------------------------------
title: Apply model change
python manage.py makemigrations app_name
#------------------------------------------------------------------------------
title: Show generate SQL
python manage.py sqlmigrate app_name migration_name
#------------------------------------------------------------------------------
#- section: Admin
#------------------------------------------------------------------------------
title: Create a super user
python manage.py createsuperuser
#------------------------------------------------------------------------------
title: Add a model to admin interface (app/admin.py)
admin.site.register(model_name)
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
title: Query operators
__exact         __iexact
__contains      __icontains
__in
__gt            __gte           __lt        __lte
__startswith    __istartswith   __endswith  __iendswith
__range
__date          __year          __iso_year
__month         __day
__week          __week_day      __iso_week_day
__quarter
__time
__hour          __minute        __second
__isnull
__regex
__iregex
#------------------------------------------------------------------------------

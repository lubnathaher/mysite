from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.db import models
from tinymce.widgets import TinyMCE
# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
    
    fieldsets = [
        ("title/date", {"fields" : ["tutorial_title","tutorial_published"]}), 
        ("content", {"fields" :["tutorial_content"]}),
        ("URLS", {"fields" :["tutorial_slug"]}),
        ("Series", {"fields" :["tutorial_series"]})
        ]
    
    formfield_overrides = {
        models.TextField: {'widget': TinyMCE()},
        }

admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)


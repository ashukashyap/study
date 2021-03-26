from django.contrib import admin
from courses.models import Lendet,Lesson,Klasa,Contact
# Register your models here.

admin.site.register(Lendet)
admin.site.register(Klasa)
admin.site.register(Contact)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    class Media:
        js = ('tiny.js',)
    
from django.contrib import admin

# Register your models here.
from resume.models import Profile


@admin.register 
class ProfileModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email','dob','state',
                  'gender','location','pimage','rdoc']
 
 
admin.site.register(Profile)

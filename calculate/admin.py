from django.contrib import admin
from calculate.models import UserProfile,Myindex,Expectedindex,IndexNumber,CourseCode,Email, Applicant
# Register your models here.





class MyIndexAdmin(admin.ModelAdmin):
	list_display = ('index','views')


class IndexAdmin(admin.ModelAdmin):
	list_display = ('index','course','post')

class CourseAdmin(admin.ModelAdmin):
	list_display = ('code','views')

class EmailAdmin(admin.ModelAdmin):
	list_display = ('name','email','message')

admin.site.register(UserProfile)
admin.site.register(Applicant)
admin.site.register(Myindex,MyIndexAdmin)
admin.site.register(Expectedindex)
admin.site.register(IndexNumber,IndexAdmin)
admin.site.register(CourseCode,CourseAdmin)
admin.site.register(Email,EmailAdmin)

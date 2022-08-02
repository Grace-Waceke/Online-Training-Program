from django.contrib import admin
from.models import Student, Community,Trainer,Course

class StudentAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name','age','email','date_of_birth','national_id','phone_number','guardian_name','guardian_contacts','country')
    search_fields=('first_name','last_name','age','email','date of birth','national id','phone number','guardian name','guardian contacts','country')
admin.site.register(Student,StudentAdmin)
admin.site.register(Community)
admin.site.register(Trainer)
admin.site.register(Course)





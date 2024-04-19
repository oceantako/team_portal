from django.contrib import admin
from .models import HumansImage,MemberWorks

class MemberWorksAdmin(admin.ModelAdmin):
    list_display = ("title", "member")

admin.site.register(HumansImage)
admin.site.register(MemberWorks, MemberWorksAdmin)


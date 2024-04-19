from django.contrib import admin
from accounts.models import User, Aikotoba


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'is_delete',)  # 一覧に出したい項目
    list_display_links = ('username', 'password',)  # 修正リンクでクリックできる項目


admin.site.register(User, UserAdmin)



class AikotobaAdmin(admin.ModelAdmin):
    list_display = ('aikotoba',)
    list_display_links = ('aikotoba',)


admin.site.register(Aikotoba, AikotobaAdmin)


# Register your models here.

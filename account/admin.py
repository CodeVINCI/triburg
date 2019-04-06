from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_admin','user_type','first_name','last_name',)
    list_display_links = ('username',)
    search_fields = ('username',)
# Register your models here.


admin.site.register(User, UserAdmin)

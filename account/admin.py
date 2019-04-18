from django.contrib import admin
from .models import User,UserRequest,Buyer,Costsheet

class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username','email','is_admin','user_type','first_name','last_name',)
    list_display_links = ('username',)
    search_fields = ('username',)
# Register your models here.


admin.site.register(User, UserAdmin)
admin.site.register(UserRequest)
admin.site.register(Buyer)
admin.site.register(Costsheet)

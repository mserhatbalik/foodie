from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile


# Register your models here.

class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()

    ordering = ('-date_joined',)

    # CHANGE THE FIELDS IN THE "LIST" PAGE.
    # list_display = ('email', 'first_name', 'last_name', 'username', 'role', 'is_active')
    readonly_fields = ('date_joined', 'last_login')

    # CHANGE THE FIELDS IN THE "ADD and MODIFY" PAGES.
    # fieldsets = (
    #     ('Meta Information', {'fields': ('username', 'email')}),
    #     ('Personal Information', {'fields': (('first_name', 'last_name'), 'phone_number', 'role')}),
    # )


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
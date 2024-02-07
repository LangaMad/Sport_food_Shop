from django.contrib import admin

# Register your models here.
# from products.admin import BasketAdmin
from .models import EmailVerification, User
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'image']
    # inlines = [BasketAdmin]

@admin.register(EmailVerification)
class EmailVerificationAdmin(admin.ModelAdmin):
    list_display = ['code', 'user', 'expiration']
    fields = ['code', 'user', 'expiration', 'created']
    readonly_fields: list[str] = ['created']



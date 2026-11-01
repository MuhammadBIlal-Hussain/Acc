from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Company, Membership, User


@admin.register(User)
class UserAdminConfig(UserAdmin):
    list_display = ("username", "email", "is_staff", "is_active")
    search_fields = ("username", "email")


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "base_currency", "is_active", "created_at")
    search_fields = ("name", "legal_name", "tax_id")
    list_filter = ("is_active", "base_currency")


@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ("user", "company", "role", "is_active")
    list_filter = ("role", "is_active")
    search_fields = ("user__username", "company__name")


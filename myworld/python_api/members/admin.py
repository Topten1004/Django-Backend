from django.contrib import admin

# Register your models here.
from .models import Member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date",)
admin.site.register(Member)
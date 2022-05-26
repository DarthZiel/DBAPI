from django.contrib import admin
from .models import User,Profile,Position,Structure
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User

    fields = ['username','password', 'fio']


admin.site.register(Profile)
admin.site.register(Position)
admin.site.register(Structure)

admin.site.site_header = "Администрация Базы данных 1 Городской поликлиники "
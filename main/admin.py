from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class MyUserAdmin(UserAdmin):
    # Колонки в списке
    list_display = ('username', 'email', 'position', 'is_in_roster', 'height', 'rating', 'is_staff')
    list_editable = ('is_in_roster',)
    list_filter = list(UserAdmin.list_filter) + ['is_in_roster', 'position']
    
    fieldsets = list(UserAdmin.fieldsets) + [
    ('Данные игрока БК ЧИТА', {
        'fields': ('is_in_roster', 'avatar', 'height', 'weight', 'position', 'rating'),
    }),
]
    

    # Аналогично для формы создания
    add_fieldsets = list(UserAdmin.add_fieldsets) + [
        ('Данные игрока БК ЧИТА', {
            'fields': ('is_in_roster', 'height', 'weight', 'position', 'rating'),
        }),
    ]


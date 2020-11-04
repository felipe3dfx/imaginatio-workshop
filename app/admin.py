from django.contrib import admin

from . import models


@admin.register(models.Category)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )

    fieldsets = (
        ('General', {
            'fields': (
                'name',
                'is_active',
            ),
        }),
    )

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(models.Product)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'category',
        'is_active',
    )

    list_filter = (
        'is_active',
        'category',
    )

    search_fields = (
        'name',
    )

    fieldsets = (
        ('General', {
            'fields': (
                'category',
                'name',
                'is_active',
            ),
        }),
    )

    autocomplete_fields = ('category',)

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True


@admin.register(models.Restaurant)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'is_active',
    )

    list_filter = (
        'is_active',
    )

    search_fields = (
        'name',
    )

    fieldsets = (
        ('General', {
            'fields': (
                'name',
                'is_active',
            ),
        }),
        ('Productos', {
            'fields': (
                'products',
            ),
        }),
    )

    filter_horizontal = ('products',)

    def has_change_permission(self, request, obj=None):
        return True

    def has_add_permission(self, request):
        return True

    def has_delete_permission(self, request, obj=None):
        return True

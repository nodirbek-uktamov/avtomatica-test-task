from django.contrib import admin

from main.models import Shop, Worker, Visit


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'worker')


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    fields = ('name', 'phone_number')


@admin.register(Visit)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ('shop__name', 'shop__worker__name')
    fields = ('datetime', 'shop', 'longitude', 'latitude')
    readonly_fields = fields

    def has_delete_permission(self, request, obj=None):
        return False

from django.contrib import admin
from .models import Produto, Vitrine


@admin.register(Vitrine)
class VitrineAdmin(admin.ModelAdmin):
    list_display = ('name', 'owner', 'slug', 'created_at')
    search_fields = ('name', 'owner__username')


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'vitrine', 'category', 'price', 'active', 'created_at')
    list_filter = ('category', 'active')
    search_fields = ('name', 'vitrine__name')

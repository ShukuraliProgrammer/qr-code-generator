from django.contrib import admin
from django.contrib.auth.models import User

from .models import QrCode, Tariff, SocialMediaChannels, Comment, Template, User

from admin_list_charts.admin import ListChartMixin
admin.site.register(User)

@admin.register(QrCode)
class QrCodeAdmin(ListChartMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('url', 'created_at', 'url_counter')
    list_filter = ('url', 'created_at', 'updated_at')
    search_fields = ('created_at', 'url', 'url_counter')

@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name',  'price', 'created_at', 'updated_at')
    list_filter = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('created_at', 'name',  'price', 'updated_at')

@admin.register(SocialMediaChannels)
class SocialMediaChannelsAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):  
    pass



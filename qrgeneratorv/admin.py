from django.contrib import admin
from django.contrib.auth.models import User
from qrgeneratorv.models import QrCode, Tariff, SocialMediaChannels, Comment, Template, User
from admin_list_charts.admin import ListChartMixin

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_staff','is_active','is_superuser', 'created_date', 'modified_date')
    search_fields = ('email', 'first_name', 'last_name')

@admin.register(QrCode)
class QrCodeAdmin(ListChartMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('admin_photo', 'url', 'created_at', 'url_counter', 'mobile', 'os', 'other_devices')
    list_filter = ('url', 'created_at', 'updated_at')
    search_fields = ('created_at', 'url', 'url_counter')
    readonly_fields = ('admin_photo',)
    def has_add_permission(self, request):
        if request.user.is_admin:
            return True
        return False
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False
    
    def has_change_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)


@admin.register(Tariff)
class TariffAdmin(admin.ModelAdmin):
    list_display = ('name',  'price', 'created_at', 'updated_at')
    list_filter = ('name', 'price', 'created_at', 'updated_at')
    search_fields = ('created_at', 'name',  'price', 'updated_at')

    def has_view_permission(self, request, obj=None):
        if request.user.is_admin or request.user.is_superuser:
            return True
        return False

@admin.register(SocialMediaChannels)
class SocialMediaChannelsAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):  
    list_display = ('social_media_type', 'social_media_type1_url_counter', 'social_media_type2', 'social_media_type2_url_counter', 'social_media_type3', 'social_media_type3_url_counter')

    def has_add_permission(self,request):
        if request.user.is_admin:
            return True
        return False
    def has_change_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False
    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(user=request.user)

    

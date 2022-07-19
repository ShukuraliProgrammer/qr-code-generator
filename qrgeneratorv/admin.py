# from itertools import count
# from django.utils import timezone 
from django.contrib import admin

from .models import QrCode
# from admincharts.admin import AdminChartMixin
# from admincharts.utils import months_between_dates
# from django.db.models import Count

# @admin.register(QrCode)
# class QrCodeAdmin(AdminChartMixin, admin.ModelAdmin):
#     def get_list_chart_data(self, queryset):
#         if not queryset:
#             return {}

#         # Cannot reorder the queryset at this point
#         earliest = min([x.created_at for x in queryset])

#         labels = []
#         totals = []
#         for b in months_between_dates(earliest, timezone.now()):
#             labels.append(b.strftime("%b %Y"))
#             totals.append(
#                 len(
#                     [
#                         x
#                         for x in queryset
#                         if x.created_at.year == b.year and x.created_at.month == b.month
#                     ]
#                 )
#             )

#         return {
#             "labels": labels,
#             "datasets": [
#                 {"label": "New accounts", "data": totals, "backgroundColor": "#18c95f","startDate":earliest},
#             ],
#         }
#     list_chart_type = "bar"
#     list_chart_data = {}
#     list_chart_options = {"aspectRatio": 6}
#     list_chart_config = None

#     def get_list_chart_queryset(self, changelist):
#         return QrCode.objects.all()


from admin_list_charts.admin import ListChartMixin
@admin.register(QrCode)
class QrCodeAdmin(ListChartMixin, admin.ModelAdmin):
    date_hierarchy = 'created_at'
    list_display = ('url', 'created_at', 'url_counter')
    list_filter = ('url', 'created_at', 'updated_at')
    search_fields = ('created_at', 'url', 'url_counter')
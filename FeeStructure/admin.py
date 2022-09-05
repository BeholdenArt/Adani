from django.contrib import admin
from FeeStructure.models import FeeFormat
from import_export.admin import ImportExportModelAdmin 

# Register your models here.

# admin.site.register(FeeFormat)


@admin.register(FeeFormat)
class FeeFormat(ImportExportModelAdmin):
    pass 

# class FeeFormat(admin.ModelAdmin):
#    readonly_fields = ('created_on', 'last_modified')
#    list_display = ('receipt_number','received_sum','date','enrolment_number','semester','stream',)
#    list_filter = ("semester", "stream")


# class FeeFormatResource(resources.ModelResource):
#     class Meta:
#         model = FeeFormat


# admin.site.register(FeeFormat, FeeFormatResource)

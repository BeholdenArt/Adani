from import_export import resources
from FeeStructure.models import FeeFormat

class FeeFormatResource(resources.ModelResource):
    class Meta: 
        import_id_fields = ('Enrollment',)
        model = FeeFormat
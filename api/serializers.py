from rest_framework.serializers import ModelSerializer
from qrgeneratorv.models import QrCode

class QrCodeSerializer(ModelSerializer):
    class Meta:
        model = QrCode
        fields = ('url', 'image')

        
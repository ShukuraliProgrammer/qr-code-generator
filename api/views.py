from rest_framework import generics
from qrgeneratorv.models import QrCode
from api.serializers import QrCodeSerializer
from qrcored.settings import ALLOWED_HOSTS
class QrCodeCreate(generics.CreateAPIView):
    queryset = QrCode.objects.all()
    serializer_class = QrCodeSerializer

    def perform_create(self, serializer):
        objects_by_user = QrCode.objects.filter(user=self.request.user).last()
        if objects_by_user.template:
            objects_by_user.template = objects_by_user.template
            objects_by_user.url = self.request.data['url']
            objects_by_user.image = serializer.validated_data['image']
            objects_by_user.save()
        elif objects_by_user:
            objects_by_user.url = self.request.data['url']
            objects_by_user.image = serializer.validated_data['image']
            objects_by_user.save()
       


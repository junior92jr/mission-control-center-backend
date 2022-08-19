from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from .serializers import ApplicationSerializer
from .models import Application


class ApplicationsViewSet(viewsets.ModelViewSet):

    serializer_class = ApplicationSerializer
    permission_classes = (AllowAny, )
    queryset = Application.objects.all()

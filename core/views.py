from rest_framework.viewsets import ModelViewSet
from rest_framework.serializers import ModelSerializer
from .models import Program


class ProgramSerializer(ModelSerializer):
    class Meta:
        model = Program
        fields = "__all__"


class ProgramViewset(ModelViewSet):
    serializer_class = ProgramSerializer
    queryset = Program.objects.all()
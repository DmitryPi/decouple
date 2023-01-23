from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import InvoiceSerializer, User, UserSerializer


class ClientList(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class InvoiceCreate(CreateAPIView):
    serializer_class = InvoiceSerializer

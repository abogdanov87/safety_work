from rest_framework import generics
from rest_framework_bulk import ListBulkCreateUpdateAPIView

from company.models import Company
from .serializers import CompanySerializer
from .filters import CompanyFilter


class CompanyListAPIView(generics.ListAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    filterset_class = CompanyFilter
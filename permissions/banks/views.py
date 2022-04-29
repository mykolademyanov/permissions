from rest_framework import viewsets
from banks.models import Bank, BankAccount
from banks.serializers import BankSerializer, BankAccountSerializer
from permissions.permissions import PermissionsViewSet, IsAnalyst, IsCustomer


class BankViewSet(PermissionsViewSet, viewsets.ModelViewSet):
    read_permissions = [IsAnalyst | IsCustomer]
    update_permissions = [IsAnalyst]

    serializer_class = BankSerializer
    queryset = Bank.objects.all()


class BankAccountViewSet(PermissionsViewSet, viewsets.ModelViewSet):
    read_permissions = [IsAnalyst | IsCustomer]
    update_permissions = [IsAnalyst | IsCustomer]

    serializer_class = BankAccountSerializer
    queryset = BankAccount.objects.all()

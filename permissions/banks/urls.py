from banks.views import BankViewSet, BankAccountViewSet
from rest_framework.routers import DefaultRouter

bank_router = DefaultRouter()
bank_router.register(r'banks', BankViewSet, basename='bank')
bank_router.register(r'bank-accounts', BankAccountViewSet, basename='bank-account')

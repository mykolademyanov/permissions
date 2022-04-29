# Permissions

1. So we have simple bank project where we have (analyst and customer)
2. Analyst can have access to Customer bank account and can change it
3. Also Customer can read and update into his own account

### Model
Analyst -> Bank -> BankAccount -> Customer

### Result
1. You can add new Bank, Customer or Analyst and it should work without code changes
2. Also we do not store permissions in the DB for every object

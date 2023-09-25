import loan_allocation
from loan_allocation.models import investors


def test_main():
    test_loans = [
        {
          "id": 12345678,
          "category": "retail",
          "risk_band": "A",
          "amount": 1000
        },
        {
          "id": 1234567,
          "category": "property",
          "risk_band": "A",
          "amount": 1000
        }
    ]
    for loan in test_loans:
        loan_allocation.create_new_loan(loan)
    
    assert len(loan_allocation.loans) == 2

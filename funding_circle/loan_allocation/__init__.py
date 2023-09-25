from loan_allocation.models import loan


loans = {}


def create_new_loan(data):
    new_loan = loan.Loan(
        loan_id=data["id"],
        category=data["category"],
        risk_band=data["risk_band"],
        amount=data["amount"]
    )
    loans[new_loan.loan_id] = new_loan
    return new_loan



def main():
    pass

if __name__ == "__main__":
    main()

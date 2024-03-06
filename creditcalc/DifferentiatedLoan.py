import math
from Loan import Loan


# This class is for differentiated loan calculations
class DifferentiatedLoan(Loan):
    def __init__(self, payment_amount, loan_amount, payment_period, interest, loan_type):
        super().__init__(loan_amount, loan_type)
        self.loan_type = loan_type
        self.interest = interest
        self.desired_repayment_period = payment_period
        self.calculated_monthly_payment_amount = payment_amount

    def process_args(self):
        self._calculate_differentiated_payment()

    def _calculate_differentiated_payment(self):
        if self.loan_amount and self.desired_repayment_period and self.interest:
            nominal_interest = self._calculate_nominal_interest()
            total_payment = 0
            for i in range(1, self.desired_repayment_period + 1):
                diff_payment = (self.loan_amount / self.desired_repayment_period + nominal_interest *
                                (self.loan_amount - self.loan_amount * (i - 1) / self.desired_repayment_period))
                print(f"Month {i}: payment is {math.ceil(diff_payment)}")
                total_payment += math.ceil(diff_payment)
            print(f"\nOverpayment = {total_payment - self.loan_amount}")


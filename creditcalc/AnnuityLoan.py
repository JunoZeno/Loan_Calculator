import math
from Loan import Loan


# This class is for annuity loan calculations
class AnnuityLoan(Loan):
    def __init__(self, payment_amount, loan_amount, payment_period, interest, loan_type):
        super().__init__(loan_amount, loan_type)
        self.loan_type = loan_type
        self.interest = interest
        self.desired_repayment_period = payment_period
        self.calculated_monthly_payment_amount = payment_amount

    def process_args(self):
        if self.desired_repayment_period is None:
            self.calculate_repayment_period()
        elif self.calculated_monthly_payment_amount is None:
            self.calculate_annuity_payment()
        elif self.loan_amount is None:
            self.calculate_loan_principal()

    def calculate_repayment_period(self):
        if self.loan_amount and self.calculated_monthly_payment_amount and self.interest:
            nominal_interest = self._calculate_nominal_interest()
            periods = math.log(self.calculated_monthly_payment_amount /
                               (self.calculated_monthly_payment_amount - nominal_interest * self.loan_amount),
                               1 + nominal_interest)
            self.desired_repayment_period = math.ceil(periods)
            self._check_months_or_years_to_repay_loan(self.desired_repayment_period)

    def _check_months_or_years_to_repay_loan(self, periods):
        if periods < 12:
            print(f"It will take {periods} months to repay this loan!")
        else:
            years = periods // 12
            months = periods % 12
            if months == 0:
                print(f"It will take {years} years to repay this loan!")
            else:
                print(f"It will take {years} years and {months} months to repay this loan!")
            self._calculate_overpayment(periods, self.calculated_monthly_payment_amount)

    def calculate_annuity_payment(self):
        if (self.loan_amount and self.desired_repayment_period and
                self.interest):
            nominal_interest = self._calculate_nominal_interest()
            annuity_payment = self.loan_amount * (
                    nominal_interest * (1 + nominal_interest) ** self.desired_repayment_period) / \
                              ((1 + nominal_interest) ** self.desired_repayment_period - 1)
            self.calculated_monthly_payment_amount = math.ceil(annuity_payment)
            print(f"Your annuity payment = {self.calculated_monthly_payment_amount}!")
            self._calculate_overpayment(self.desired_repayment_period, self.calculated_monthly_payment_amount)

    def calculate_loan_principal(self):
        nominal_interest = self._calculate_nominal_interest()
        self.loan_amount = self.calculated_monthly_payment_amount * (
                (1 + nominal_interest) ** self.desired_repayment_period - 1) / (
                                   nominal_interest * (1 + nominal_interest) ** self.desired_repayment_period)
        self.loan_amount = math.floor(self.loan_amount)
        print(f"Your loan principal = {self.loan_amount}!")
        self._calculate_overpayment(self.desired_repayment_period, self.calculated_monthly_payment_amount)

    def _calculate_overpayment(self, periods, monthly_payment):
        overpayment = periods * monthly_payment - self.loan_amount
        print(f"Overpayment = {overpayment}")

import math


class Loan:
    def __init__(self, loan_amount, calculation_option):
        self.loan_amount: int = loan_amount
        self.calculation_option: str = calculation_option

        self.desired_monthly_payment_amount: int = None  # private
        self.calculated_repayment_period: int = None  # private

        self.desired_repayment_period: int = None  # private
        self.calculated_monthly_payment_amount: int = None  # private
        self.final_monthly_payment: int = None  # private

    def process_loan_query_choice(self):
        if self.calculation_option == "m":
            self.calculate_monthly_payment()

        elif self.calculation_option == "p":
            self.calculate_repayment_period_in_months()

        else:
            print("Invalid selection. Please enter either m or p")

    def calculate_repayment_period_in_months(self):
        self.desired_repayment_period = int(input("Enter the number of months:\n"))
        uncalculated_monthly_payment = self.loan_amount / self.desired_repayment_period
        if uncalculated_monthly_payment.is_integer():
            self.calculated_monthly_payment_amount = int(uncalculated_monthly_payment)
            print(f'\nYour monthly payment = {self.calculated_monthly_payment_amount}')
        else:
            self.calculated_monthly_payment_amount = math.ceil(uncalculated_monthly_payment)
            self.final_monthly_payment = self.loan_amount - (self.calculated_monthly_payment_amount *
                                                             (self.desired_repayment_period - 1))
            print(f'\nYour monthly payment = {self.calculated_monthly_payment_amount} '
                  f'and the last payment = {self.final_monthly_payment}.')

    def calculate_monthly_payment(self):
        self.desired_monthly_payment_amount = int(input("Enter monthly payment:\n"))
        non_rounded_repayment_period = self.loan_amount / self.desired_monthly_payment_amount
        self.calculated_monthly_payment_amount = round(non_rounded_repayment_period)
        if self.calculated_monthly_payment_amount > 1:
            print(f'\nIt will take {self.calculated_monthly_payment_amount} months to repay the loan')
        else:
            print(f'\nIt will take {self.calculated_monthly_payment_amount} month to repay the loan')

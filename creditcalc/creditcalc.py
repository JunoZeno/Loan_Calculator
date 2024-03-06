import argparse

from AnnuityLoan import AnnuityLoan
from DifferentiatedLoan import DifferentiatedLoan

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="This program calculates the monthly payment, number of payments, "
                                                 "and loan principal.")
    parser.add_argument("--type", type=str, help="Type of payment: annuity or diff")
    parser.add_argument("--payment", type=float, help="The monthly payment amount.")
    parser.add_argument("--principal", type=float, help="The loan principal amount.")
    parser.add_argument("--periods", type=int, help="The number of periods needed to repay the loan.")
    parser.add_argument("--interest", type=float, help="The loan interest rate.")

    args = parser.parse_args()

    # Counting Parameters
    count_parameters = 0

    # Check if any of the parameters are negative
    params_has_negative_values = False

    # Loop through the arguments and count the number of parameters and check if any of the parameters are negative
    for arg in vars(args):
        if getattr(args, arg) is not None:
            count_parameters += 1
            current_value = getattr(args, arg)
            if (isinstance(current_value, int) or isinstance(current_value, float)) and current_value < 0:
                params_has_negative_values = True
                break

    is_four_or_more_params = count_parameters >= 4

    if (args.type is None
            or args.interest is None
            or (args.type == "diff" and args.payment is not None)
            or is_four_or_more_params is False
            or params_has_negative_values is True):
        print("Incorrect parameters")
    else:
        # annuity calculation
        if args.type == "annuity":
            new_annuity_loan = AnnuityLoan(args.payment, args.principal, args.periods, args.interest, args.type)
            new_annuity_loan.process_args()
        # diff calculation
        elif args.type == "diff":
            new_diff_loan = DifferentiatedLoan(args.payment, args.principal, args.periods, args.interest, args.type)
            new_diff_loan.process_args()

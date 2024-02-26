import Loan

# Where interaction with user begins
principal_amount = int(input("Enter the loan principal:\n"))

user_choice = input('What do you want to calculate?\n'
                    'type "m" for number of monthly payments,\n'
                    'type "p" for the monthly payment:\n').lower()

new_loan = Loan.Loan(principal_amount, user_choice)
new_loan.process_loan_query_choice()


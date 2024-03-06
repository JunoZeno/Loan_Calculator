## Annuity and Differential Payment Calculator

This Python program calculates both annuity and differential payments for loans, along with the number of months required to pay off the loan and the overpayment compared to the original loan amount.

### Features:
- **Annuity Payment Calculation:** Calculate the fixed monthly payment for a loan with a fixed interest rate and term.
- **Differential Payment Calculation:** Calculate payments where the principal portion decreases monthly while the interest remains constant.
- **Loan Term Calculation:** Determine the number of months required to pay off the loan.
- **Overpayment Analysis:** Determine the total amount paid over the original loan amount.

### Usage:
- Input the loan amount, interest rate, loan type ("diff" or "annuity"), and loan term to calculate annuity and differential payments.
- View the calculated payments and the total months needed to pay off the loan.
- Analyze the overpayment compared to the original loan amount.

### Why Use This Program:
- **Financial Planning:** Plan your loan payments effectively by understanding the monthly payment structures for both annuity and differential payment methods.
- **Cost Analysis:** Gain insights into the total cost of the loan, including interest payments and overpayment compared to the original loan amount.
- **Educational Purposes:** Understand the mechanics of loan payments and amortization schedules through hands-on calculations.

### How to Run:
1. Clone the repository to your local machine.
2. Navigate to the `creditcalc` directory in your terminal.
3. Run the Python script `creditcalc.py`.
4. Follow the below provided examples to input loan details and view the calculated payments and analysis.

### Examples:

#### Differentiated Payment:

```python
> python3 creditcalc.py --type=diff --principal=1000000 --periods=10 --interest=10
Month 1: payment is 108334
Month 2: payment is 107500
Month 3: payment is 106667
Month 4: payment is 105834
Month 5: payment is 105000
Month 6: payment is 104167
Month 7: payment is 103334
Month 8: payment is 102500
Month 9: payment is 101667
Month 10: payment is 100834


Overpayment = 45837
```

#### Annuity Payment:
```python
> python creditcalc.py --type=annuity --principal=1000000 --periods=60 --interest=10
Your annuity payment = 21248!
Overpayment = 274880
```

### Acknowledgments:
- This project was created based on a project provided in the HyperSkill Jetbrains academy Python OOP course.
- Github Copilot was leveraged in the creation of this project.
- the Argparse module was used

## Permissions:
- If you'd like access to this repo or you'd like to improve upon this project please let me know. 

## Cheers and thanks for checking out my project!

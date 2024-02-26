from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
import re

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)


class LoanCalcTest(StageTest):
    def generate(self):
        return [
            TestCase(
                stdin='1000\nm\n200',
                attach=(5, 'months'),
            ),
            TestCase(
                stdin='1000\nm\n150',
                attach=(7, 'months'),
            ),
            TestCase(
                stdin='1000\nm\n1000',
                attach=(1, 'month'),
            ),
            TestCase(
                stdin='1000\np\n10',
                attach=100,
            ),
            TestCase(
                stdin='1000\np\n9',
                attach=['112', '104'],
            ),
            TestCase(
                stdin='1350\nm\n140',
                attach=(10, 'months'),
            ),
            TestCase(
                stdin='300\nm\n400',
                attach=(1, 'month'),
            ),
            TestCase(
                stdin='5555\np\n11',
                attach=505,
            ),
            TestCase(
                stdin='5576\np\n10',
                attach=['558', '554'],
            ),
        ]

    def check(self, reply, attach):
        reply = reply.lower()
        if isinstance(attach, tuple):
            a, b = attach
            if a == 1:
                if '1 months' in reply.splitlines()[-1]:
                    output = '{0} should be in the output, but you have output {1}.\n' \
                             'Please use the singular form of the word "month" in this case.'
                    return CheckResult.wrong(
                        output.format('1 month', '1 months'),
                    )

            if str(a) not in reply or b not in reply.lower():
                output = (
                    '"{0} {1}" should be in the output, but you output {2}'
                )
                return CheckResult.wrong(
                    output.format(a, b, reply),
                )

        elif isinstance(attach, list):
            if attach[0] not in reply or attach[1] not in reply:
                numbers = re.findall(r'[-+]?(\d*\.\d+|\d+)', reply)
                if len(numbers) == 0:
                    output = (
                        'The correct monthly payment is {0}, and the last payment is'
                        ' {1}, but there are no numbers in your output'
                        .format(attach[0], attach[1])
                    )
                elif len(numbers) == 1:
                    output = (
                        'The correct monthly payment is {0}, and the last payment is'
                        ' {1}, but there is only {2} in your output'
                        .format(attach[0], attach[1], numbers[0])
                    )
                else:
                    output = (
                        'The correct monthly payment is {0}, and the last payment is'
                        ' {1}, but there are {2} and {3} in your output'
                        .format(attach[0], attach[1], numbers[0], numbers[1])
                    )
                return CheckResult.wrong(output)
        else:
            if str(attach) not in reply:
                output = (
                    'The correct monthly payment is {0}. But in your output it is {1}'
                )
                return CheckResult.wrong(
                    output.format(attach, reply),
                )

        return CheckResult.correct()


if __name__ == '__main__':
    LoanCalcTest('creditcalc.creditcalc').run_tests()

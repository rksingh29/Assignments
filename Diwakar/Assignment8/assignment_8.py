import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(module)s:%(levelname)s::::::%(message)s")
handler = logging.FileHandler('my_log.txt')
handler.setFormatter(formatter)
logger.addHandler(handler)


class CustomException(Exception):
    pass


class Income:

    def __init__(self, salary, expense):
        self._savings = None
        self._salary = salary
        self._expense = expense
        #self.savings

        logger.info("Salary is :{}".format(self.salary))
        logger.info("Expense is :{}".format(self.expense))

    @property
    def salary(self):
        return self._salary

    @property
    def expense(self):
        return self._expense

    def savings(self):
        try:
            self._savings = self.salary - self.expense
            if self._savings > 0:
                logger.info('Savings is :{}'.format(self._savings))
            else:
                raise CustomException
        except CustomException:
            logger.exception("Savings cannot be negative")
            
    @salary.setter
    def salary(self, value):
        self._salary = value

    @expense.setter
    def expense(self, value):
        self._expense = value


em1 = Income(34000, 20000)
em1.savings()

em2 = Income(20000, 30000)
em2.savings()

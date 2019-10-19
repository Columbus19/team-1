import customers as c
import MockParser as MP
import random
import math as m

Customers = MP.getCustomers()

def debtPaymentPlanner(payment): # Entered as a montly amount
    randCustomer = random.choice(Customers)
    debt = randCustomer.getDebt()
    paymentsAmount = m.ceil(int(debt)/int(payment))
    return int(paymentsAmount) # output as months

Test = debtPaymentPlanner('500') # Testing
print(Test)
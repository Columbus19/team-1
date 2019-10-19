def getStatus(creditScore, missedLastPayment):
    if creditScore < 600 and missedLastPayment == False:
        return "Fair" # Standing
    if creditScore < 600 and missedLastPayment == True:
        return "Poor" # Standing
    if creditScore > 600 and missedLastPayment == False:
        return "Excellent" # Standing
    if creditScore > 600 and missedLastPayment == True:
        return "Good" # Standing


# Customer Class 
class Customer():
    def __init__(self, id=None, fName=None, lName=None, email=None, gender=None, address=None, creditScore=None, missedLastPayment=None, income=None):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.email = email
        self.gender = gender
        self.address = address
        self.creditScore = creditScore
        self.missedLastPayment = missedLastPayment
        self.status = getStatus(creditScore, missedLastPayment)
        self.income = float(income)
        self.budget = float(income)*0.8 / 12 # Savings of 20%
        self.debt = float(income) * 1.5

    def getIncome(self):
        return self.income
    
    def getFullName(self):
        return str(self.fName + " " + self.lName)

    def getCreditScore(self):
        return int(self.creditScore)

    def getEmail(self):
        return str(self.email)

    def getBudget(self):
        return float(self.budget)

    def getDebt(self):
        return float(self.debt)

    def getId(self):
        return int(self.id)

    def notify(self):
        if self.status == "Good":
            return "Please stay up to date with your payments :)"
        if self.status == "Excellent":
            return "You're doing excellent keep it up!"
        if self.status == "Poor":
            return "To improve your credit score it is crucial to make your payments on time. You got this!"
        if self.status == "Fair":
            return "Keep up the good work!"

    def printOut(self):
        print("Customer: " + str(self.fName) + " " + str(self.lName))
        print("Email: " + str(self.email))
        print("Gender: " + str(self.gender))
        print("Address: " + str(self.address))
        print("Credit Score: " + str(self.creditScore))
        print("Missed Last Payment: " + str(self.missedLastPayment))
        print("Overall Standing: " + str(self.status))

    
    
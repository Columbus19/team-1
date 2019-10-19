
# Customer Class 
class Customer():
    def getStatus(self, creditScore, missedLastPayment):
        if creditScore < 600 and missedLastPayment == False:
            return "Fair" # Standing
        if creditScore < 600 and missedLastPayment == True:
            return "Poor" # Standing
        if creditScore > 600 and missedLastPayment == False:
            return "Excellent" # Standing
        if creditScore > 600 and missedLastPayment == True:
            return "Good" # Standing

    def __init__(self, id=None, fName=None, lName=None, email=None, gender=None, address=None, creditScore=None, missedLastPayment=None):
        self.id = id
        self.fName = fName
        self.lName = lName
        self.email = email
        self.gender = gender
        self.address = address
        self.creditScore = creditScore
        self.missedLastPayment = missedLastPayment
        self.status = getStatus(creditScore, missedLastPayment)

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

    



    
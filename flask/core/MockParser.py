import csv
import random
import customers as c

listOfCustomers = []

#list of incomes for customers to compare customers with each other
listOfIncomes = []

#list of credit scores for customers
listOfCreditScores = []

def parseData(file):
    #list filled with lines
    items = []
    text = open(file, "r")
    lines = text.readlines()
    for line in lines:
        items = line.split(",")
        id = items[0]
        firstName = items[1]
        lastName = items[2]
        email = items[3]
        gender =  items[4]
        address = items[5]
        creditScore = items[6]
        missedPayment = items[7]
        income = items[8]
        cust = c.Customer(id, firstName, lastName, email, gender, address, creditScore, missedPayment, income)
        listOfCustomers.append(cust)
        listOfIncomes.append(cust.getIncome())  #implemented using a get method to maintain modularity
        listOfCreditScores.append(cust.getCreditScore())


'''
def generateSSN(file):
    parse(file)
    text = open(file, "r")
    lines = text.readlines()
    for line in lines:
        num = random.randint(100000000, 999999999)
        customer[index] = num
'''

parseData("flask/static/MOCK_DATA.csv")
print(listOfCustomers)
print(listOfIncomes)
print(listOfCreditScores)


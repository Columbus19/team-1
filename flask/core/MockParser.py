import csv
import random
import customers as c

listOfCustomers = []

def parse(file):
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
        listOfCustomers.append(c.Customer(id, firstName, lastName, email, gender, address, creditScore))

'''
def generateSSN(file):
    parse(file)
    text = open(file, "r")
    lines = text.readlines()
    for line in lines:
        num = random.randint(100000000, 999999999)
        customer[index] = num
'''




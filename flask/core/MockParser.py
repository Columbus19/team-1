import csv
import random

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
        ssn = items[7]

        #TODO: call customer method with these variables above as arguments

        

def generateSSN(file):
    parse(file)
    text = open(file, "r")
    lines = text.readlines()
    for line in lines:
        num = random.randint(100000000, 999999999)
        customer[index] = num




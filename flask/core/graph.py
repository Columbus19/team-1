import matplotlib.pyplot as plt 
import MockParser as MP

# plotting a histogram
MP.parseData("flask/static/MOCK_DATA.csv")
income = MP.getIncomes()
budget = MP.getBudgets()
creditScore = MP.getCreditScores()

def budgetIncome():
    #budget vs income
    plt.scatter(income, budget, color = 'green', alpha = 0.5)
    
    # x-axis label 
    plt.xlabel('Income') 
    # frequency label 
    plt.ylabel('Budget') 
    # plot title 
    plt.title('Budget vs Income') 
    
    # function to show the plot 
    plt.show()

def creditScoreIncome():
    #budget vs income
    plt.scatter(income, creditScore, color = 'blue', alpha = 0.5)
    
    # x-axis label 
    plt.xlabel('Income') 
    # frequency label 
    plt.ylabel('Credit Score') 
    # plot title 
    plt.title('Credit Score vs Income') 
    
    # function to show the plot 
    plt.show()

budgetIncome()
creditScoreIncome()
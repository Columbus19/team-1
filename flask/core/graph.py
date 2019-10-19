import matplotlib.pyplot as plt 
import MockParser as MP

# plotting a histogram
income = MP.getIncomes()
budget = MP.getBudgets()
creditScore = MP.getCreditScores()

def budgetIncome():
    #budget vs income
    plt.hist(income, budget, color = 'green', histtype = 'bar', rwidth = 0.8)
    
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
import math

#Start text
intro = """
=============================================================================
Choose either 'investment' or 'bond' from the menu below to proceed:
-----------------------------------------------------------------------------
1. investment   : to calculate the amount of interest you'll earn interest.

2. bond         : to claculate the amount you'll have to pay on a home loan.
=============================================================================
"""

#-------------------------INVESTMENT-------------------------#
#Method calculating simple interest
def simple_interest(depositamount, interestrate, years):
    #Converging percentage to decimal
    interest = interestrate/100
    finalvalue = depositamount * (1 + interest * years)
    return finalvalue
#End Method===================================================

#Method calculating compound interest
def compound_interest(depositamount, interestrate, years):
    #Converging percentage to decimal
    interest = interestrate/100
    finalvalue = depositamount * math.pow((1 + interest), years)
    return finalvalue
#End Method===================================================

#Method for investment input and final output
def investment():
    
    investment_type = ""
    deposit_amount = float(input("Deposit amount:\t\t\t\tR"))
    print("-----------------------------------------------------------------------------")
    interest_rate = float(input("Interest rate (e.g.: 0 - 100):\t\t"))
    print("-----------------------------------------------------------------------------")
    years = float(input("Investment years:\t\t\t"))
    print("-----------------------------------------------------------------------------")
    #Decides whether the calculator needs to use the simple or compound interest method
    investment_type = input("Is your investment 'simple' or 'compound': \t").lower()
    if investment_type == "simple":
        final_value = simple_interest(deposit_amount, interest_rate, years)
    if investment_type == "compound":
        final_value = compound_interest(deposit_amount, interest_rate, years)
    
    #prints final value
    print("=============================================================================\nThe final payoff value is: R", final_value, "\n=============================================================================")
#End Method===================================================

#----------------------------BOND----------------------------#
def bond():
    original_value = float(input("Building's original value:\t\t\tR"))
    print("-----------------------------------------------------------------------------")
    interest_rate = float(input("Interest rate (e.g.: 0 - 100):\t\t\t"))
    print("-----------------------------------------------------------------------------")
    repayment_months = float(input("Bond's repayment months:\t\t\t"))
    
    #Converging percentage to decimal
    interest = interest_rate/100
    monthly_repayment = (original_value * (interest / 12)) / (1 - (math.pow((1 + (interest / 12)), -repayment_months)))

    total_repayment = monthly_repayment*repayment_months

    #prints final value
    print("=============================================================================\nMonthly installations:\tR", monthly_repayment, "\n-----------------------------------------------------------------------------\nTotal repayment:\tR", total_repayment,"\n=============================================================================")
#End Method===================================================

#Main method
def main():

    ans = ""

    # ans1 = input(intro + "\nYour answer:\t").lower()

    while (ans != "bond" or ans != "investment") == True:
        ans = input("Invalid selection!\n\n" + intro + "\nYour answer:\t").lower()
        if(ans == "bond" or ans == "investment"):
            break

    if ans == "investment":
        investment()
    
    if ans == "bond":
        bond()

    print("\nDone!\n\n")
#End Method===================================================

main()
class ReturnOnInvestment():

    def __init__(self):
        self.monthlyRentalIncome = 0
        self.totalInvestment = 0
        self.totalExpenses = 0
        self.purchasePrice = 0
        self.roi = 0

    def houseInfo(self):
        
        self.purchasePrice = int(input("What is the purchase price of the property?: "))
        #Income
        self.monthlyRentalIncome = int(input("How much rent would you like to charge a month?: "))
        if self.purchasePrice > 0 and self.monthlyRentalIncome > 0:
            self.totalInvestmentCalc()
            self.totalExpensesCalc()
            self.roiCalc()
        else:
            print("Invalid Input")
            return

    def totalInvestmentCalc(self):
        
        downPayment = int(input("How much down payment did you place?: "))
        closingCosts = int(input("How much were closing costs?: "))
        repairBudget = int(input("How much did you spend on repairs?: "))
        misc = int(input("How much other significant payments did you do?: "))

        self.totalInvestment = downPayment + closingCosts + repairBudget + misc

    def totalExpensesCalc(self):
        
         #Expenses
        tax = int(input("What are the taxes?: "))
        insurance = int(input("What are you paying in insurance?: "))
        utilities = int(input("How much do you pay in utilities?: "))
        hoa = int(input("How much do you pay in HOA fees?: "))
        outdoors = int(input("How much do you pay in outdoor upkeep such as lawn or snow?: "))
        vacancy = int(input("How much will you pay when rental property is not being used?: "))
        repairs = int(input("How much are you paying in repairs?: "))
        capEx = int(input("How much are you putting aside for captital expenditures?: "))
        propertyManagement = int(input("How much are you paying in property management?: "))
        mortgage = int(input("How much do you pay to mortgage?: "))

        self.totalExpenses = tax + insurance + utilities + hoa + outdoors + vacancy + repairs + capEx + propertyManagement + mortgage

    def roiCalc(self):         

        #cash flow
        monthlyCashFlow = self.monthlyRentalIncome - self.totalExpenses

        #cash on cash return on investment
        annualCashFlow = monthlyCashFlow * 12
        self.roi = (annualCashFlow / self.totalInvestment) * 100
        roundedROI = round(self.roi, 2)

        print(f"\nYou purchased the property for ${self.purchasePrice}")
        print(f"Your total investment is ${self.totalInvestment}")
        print(f"Your monthly rental income is ${self.monthlyRentalIncome}")
        print(f"Your total monthly expenses is ${self.totalExpenses}")
        print(f"Your monthly cash flow is ${monthlyCashFlow}")
        print(f"Your annual cash flow is ${annualCashFlow}")
        
        print(f"\nYour return on investment is {roundedROI}%.")

    def run(self):

        while True:
            prompt = input("""\n
            Welcome to Bigger Pockets Rental Property Calculator!
            What would you like to do?
            
            [C]alculate Return on Investment and See Comparison
            [Q]uit
            
            """)

            if prompt.lower() == "c":
                self.houseInfo()
            elif prompt.lower() == "q":
                print("Thank you for using Bigger Pockets Rental Property Calculator!")
                break
            else:
                print("Incorrect Input... Try Again")

biggerPockets = ReturnOnInvestment()
biggerPockets.run()

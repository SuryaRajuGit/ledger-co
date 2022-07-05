from FixedValues import Values

import math
class Loan:
    def __init__(self):
        self.loanDetails = {}
        self.isLumpSumPaid = {} 
        self.lumpSumpDetais = {}
    def emi_calucation(self,BANK_NAME,BORROWER_NAME,PRINCIPAL,NO_OF_YEARS,RATE_OF_INTEREST):
        """calculation EMI for borrowed amount 

        Args:
            BORROWER_NAME (string): name of the Borrower 
            PRINCIPAL (integer): borrowed amount
            NO_OF_YEARS (integer): no of years 
            RATE_OF_INTEREST (integer): rate of interest for the borrowed ammount

        Returns:
            _type_: _description_
        """
        INTEREST = math.ceil(PRINCIPAL * NO_OF_YEARS * RATE_OF_INTEREST) / Values.Hundered # intrest calculation
        AMOUTNT = INTEREST + PRINCIPAL     # amount calculation
        self.loanDetails[BANK_NAME] = {}
        self.loanDetails[BANK_NAME]["AMOUTNT"] = AMOUTNT  # storing AMOUNT details 
        EMI = math.ceil(AMOUTNT / (NO_OF_YEARS * Values.MonthsInAYear))
        return EMI
     
    def loan_details(self,input_values):
        
        BANK_NAME = input_values[0]
        BORROWER_NAME = input_values[1]
        [PRINCIPAL,NO_OF_YEARS,RATE_OF_INTEREST] = list(map(int,input_values[2:]))
        """Calucating AMOUNT = PRINCIPLE + INTREST and storing in dictonary  

        Args:
            BANK_NAME (string ): name of the band from money borrowed
            BORROWER_NAME (string): name of the Borrower
            PRINCIPAL (integer): borrowed amount
            NO_OF_YEARS (integer): no of years
            RATE_OF_INTEREST (integer): rate of interest for the borrowed ammount
        """
        EMI = self.emi_calucation(BANK_NAME,BORROWER_NAME,PRINCIPAL,NO_OF_YEARS,RATE_OF_INTEREST) # calling emi_calucation for getting EMI 
        
        self.loanDetails[BANK_NAME][BORROWER_NAME] = BORROWER_NAME
        self.loanDetails[BANK_NAME]["EMI"] = EMI   # storing EMI value in loan_details 
        self.loanDetails[BANK_NAME]["amountToBePayed"] = EMI * (int(NO_OF_YEARS) *Values.MonthsInAYear) #  storeing total payable amount

    def lump_sum_payment(self,input_values): 
        
        [BANK_NAME,BORROWER_NAME,LUMP,EMI_NO] = input_values
        """storing given lumpsum at which EMI payed 

        Args:
            BANK_NAME (string ): name of the band from money borrowed
            BORROWER_NAME (string): name of the Borrower
            LUMP (integer): LUMP (integer): payed lumpsum
            EMI_NO (inteer): lumpsum payed along with this EMI 
        """
        self.lumpSumpDetais[BANK_NAME] = {}
        self.lumpSumpDetais[BANK_NAME]["LUMP"] = int(LUMP)  # storing payed lump sum value
        self.lumpSumpDetais[BANK_NAME]["EMI_NO"] = int(EMI_NO)    # stroring corresponding lump sum payed  EMI 
       
    def nearest_value(self,amountToPay,input_values):
        """caluation to nearest value if the remaineder is less than 50 or not 

        Args:
            amountToPay (integer):remaining  amount need to be payed by boorower

        Returns:
            EMIS: remaining emi's
        """

        [BANK_NAME,BORROWER_NAME,NO_OF_MONTHS] = input_values 
        val = 50 
        if amountToPay % self.loanDetails[BANK_NAME]["EMI"] > val:
            EMIS = math.ceil(round(amountToPay / self.loanDetails[BANK_NAME]["EMI"],1)) 
             
        else:
            EMIS = round(amountToPay / self.loanDetails[BANK_NAME]["EMI"])

        return EMIS
            
    def amount_calcuation(self,input_values,LUMP):
        
        [BANK_NAME,BORROWER_NAME,NO_OF_MONTHS] = input_values
        """caluating amount payed upto given months and emis remaining

        Args:
            BANK_NAME (string ): name of the band from money borrowed
            LUMP (integer): payed lumpsum 
            BORROWER_NAME (string): name of the Borrower
            NO_OF_MONTHS (integer):months after lumpsum payed 

        Returns:
           totalPayedAmount (integer):  total payed amount + lumpsum
           emisToPay (integer) :  remianing EMIS to be payed
        """
        totalPayedAmount = LUMP + ( self.loanDetails[BANK_NAME]["EMI"]) * int(NO_OF_MONTHS) # added lumpsum and emis payed upto given month
        amountToPay =  self.loanDetails[BANK_NAME]["amountToBePayed"] - totalPayedAmount # calucated remaning amount to pay
        emisToPay = self.nearest_value(amountToPay,input_values) 

        return totalPayedAmount,emisToPay

    def balance_emis(self,input_values): 
        
        [BANK_NAME,BORROWER_NAME,NO_OF_MONTHS] = input_values
        """printing payed emis upto the given month 

        
        Returns:
            BANK_NAME (string ): name of the band from money borrowed
            BORROWER_NAME (string): name of the Borrower
            totalPayedAmount (integer):  total payed amount + lumpsum
            emisToPay (integer) :  remianing EMIS to be payed
        """
 
        
        # #lumpSumPayedMonth = int(NO_OF_MONTHS)+1 if self.lumpSumpDetais.get(BANK_NAME) == None else self.lumpSumpDetais[BANK_NAME].get("EMI_NO")  
        try:
            lumpSumPayedMonth = self.lumpSumpDetais[BANK_NAME]["EMI_NO"]
            
        except:
            lumpSumPayedMonth = int(NO_OF_MONTHS)+1
            
        
        if lumpSumPayedMonth <= int(NO_OF_MONTHS): # condition if lumpsum is payed by the borrower with in the given month
            LUMP = self.lumpSumpDetais[BANK_NAME]["LUMP"]
            totalPayedAmount,emisToPay = self.amount_calcuation(input_values,LUMP) 
            # if totalPayedAmount > self.loanDetails[BANK_NAME]["AMOUTNT"]  :
            #     totalPayedAmount = math.ceil(self.loanDetails[BANK_NAME]["AMOUTNT"])
            
        else:   # no lump sum payed with the given month 
            LUMP = 0
            totalPayedAmount,emisToPay = self.amount_calcuation(input_values,LUMP)
        
        
        return BANK_NAME,BORROWER_NAME,totalPayedAmount,emisToPay 
    
    





    
    
    
    
        
        
        
        






        
        
        
        
        
        
    
    
    



    
    
        
        
        
        
    
    
    
    
    
    

        
        
        
        
        
        
        
        





        

        
        
        
        
        
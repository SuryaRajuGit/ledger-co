
from loan import Loan 
import sys 

def main():
    input_file = sys.argv[1]
    parser =open(input_file,"r")
    
    # parser = ["LOAN IDIDI Dale 5000 1 6","BALANCE IDIDI Dale 6"]
    loanObject = Loan()
    for line in parser:
        inputCommand = line.split(" ") 
        if inputCommand[0] == "LOAN":
            loanObject.loan_details(inputCommand[1:])
        elif inputCommand[0] == "PAYMENT":
            loanObject.lump_sum_payment(inputCommand[1:])
        else:
            BANK_NAME,BORROWER_NAME,totalPayedAmount,emisToPay = loanObject.balance_emis(inputCommand[1:]) 
            print(BANK_NAME,BORROWER_NAME,totalPayedAmount,emisToPay)
            
            
if __name__ == "__main__":
    main()








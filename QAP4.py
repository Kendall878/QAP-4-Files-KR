import time
from datetime import datetime

InvoiceDate = datetime.now()
# Makes the first letter convert to uppercase
def to_title_case(name):
    return ' '.join(word.capitalize() for word in name.split())

ProvinceLst = ["NL", "PE", "NS", "NB", "QC", "ON", "MB", "SK", "AB", "BC", "YT", "NT", "NU"]
PayOptions = ["Full", "Monthly", "Down Pay"]

# Validates date input
def validate_date(date_input, date_type):
    allowed_char = set("1234567890/")
    if date_input == "":
        print(f"Error: {date_type} Cannot be Blank.")
        return False
    elif not set(date_input).issubset(allowed_char):
        print(f"Error: {date_type} Can Only Contain Numbers and /")
        return False
    return True

while True:
    allowed_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
    while True:
        CustomerFirst = input("Enter Customer First Name, or (END) to end: ")
        if CustomerFirst == "":
            print("Error: Customer Name Cannot be Blank.")
        elif set(CustomerFirst).issubset(allowed_char) == False:
            print("Error: Customer Name Cannot Contain Special Characters or Numbers.")
        elif CustomerFirst == "END":
            print("Program Terminated")
            exit()
        else:
            CustomerFirst = to_title_case(CustomerFirst)
            break

    while True:
        allowed_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ ")
        CustomerLast = input("Enter Customer Last Name: ")
        if CustomerLast == "":
            print("Error: Customer Name Cannot be Blank.")
        elif set(CustomerLast).issubset(allowed_char) == False:
            print("Error: Customer Name Cannot Contain Special Characters or Numbers.")
        else:
            CustomerFirst = to_title_case(CustomerLast)
            break
    while True:
        allowed_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'- ")
        CustAddress = input("Enter Customer Address: ")
        if CustAddress == "":
            print("Error: Customer Address Cannot be Blank")
        elif set(CustAddress).issubset(allowed_char) == False:
            print("Error: Customer Address Cannor Contain Special Characters")
        else:
            CustAddress = to_title_case(CustAddress)
            break

    while True:
        allowed_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'. ")
        City = input("Enter Customer City: ")
        if City == "":
            print("Error: Customer City Cannot be Blank")
        elif set(City).issubset(allowed_char) == False:
            print("Error: Customer City Cannot Contain Special Characters")
        else:
            City = to_title_case(City)
            break

    while True:
        allowed_char = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        Province = input("Enter Customer Province(Initials Only): ").upper()
        if Province == "":
            print("Error: Province Cannot be Blank")
        elif set(Province).issubset(allowed_char) == False:
            print("Error: Province Cannot Contain Numbers or Special Characters")
        elif Province not in ProvinceLst:
            print("Error: Not a Valid Province")
        else:
            break

    while True:
        allowed_char = set("1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        PostalCode = input("Enter Customer Postal Code: ")
        if PostalCode == "":
            print("Error: Cannot be Blanl")
        elif set(PostalCode).issubset(allowed_char) == False:
            print("Error: Postal Code Cannot Contain Special Characters")
        elif len(PostalCode) !=6:
            print("Error: Postal Code Must be 6 Digits Long")
        else:
            break
    while True:
        allowed_char = set("1234567890")
        PhoneNum = input("Enter Customer Phone Number: ")
        if PhoneNum == "":
            print("Error: Cannot be Blank")
        elif set(PhoneNum).issubset(allowed_char) == False:
            print("Error: Phone Number Can Only Contain Numbers")
        elif len(PhoneNum) !=10:
            print("Error: Phone Number Must be 10 Digits Long")
        else:
            break

    while True:
        CarinsNum = int(input("Enter Number of Cars Being Insured: "))
        if CarinsNum == "":
            print("Error: Cannot be Blank")
        else:
            try:
                CarinsNum = int(CarinsNum)
                break
            except ValueError:
                print("Error: Please Enter a Valid Number")

    while True:
        ExtraLiab = input("Would The Customer Like Extra Liability up to $1,000,000 (Enter Y For Yes or N For No): ").upper()
        if ExtraLiab != "Y" and ExtraLiab != "N":
            print("This Option Can Only be Y or N")
        else:
            break
    while True:
        GlassCov = input("Would The Customer Like Glass Coverage (Y For Yes And N For No): ").upper()
        if GlassCov != "Y" and GlassCov != "N":
            print("This Option Can Only be Y or N")
        else:
            break

    while True:
        LoanCar = input("Would The Customer Like a Lonar Car (Enter Y For Yes or N For No): ").upper()
        if LoanCar != "Y" and LoanCar != "N":
            print("This Option Can Only be Y or N")
        else:
            break

    while True:
        PayType = input("Enter if Car Will be Paid in Full, Monthly, or Down Pay: ")
        if PayType not in PayOptions:
            print("Error: Please Enter a Valid Payment Type (Full, Monthly, Down Pay)")
        else:
            break

    if PayType == "Down Pay":
        while True:
            allowed_char = set("1234567890")
            PayAmt = input("Enter Amount Of The Payment: ")
            if PayType == "":
                print("Error: Pay Amount Cannot Be Blank")
            elif set(PayAmt).issubset(allowed_char) == False:
                print("Error: Only Numbers Can be Entered")
            else:
                break



    while True:
        allowed_char = set("1234567890")
        ClaimNum = input("Enter Claim Number: ")
        if ClaimNum == "":
            print("Error: Cannot be Blank")
        elif set(ClaimNum).issubset(allowed_char) == False:
            print("Error: Claim Number Can Only Contain Numbers")
        elif len(ClaimNum) !=5:
            print("Error: Claim Number Must be 10 Digits Long")
        else:
            break
        

    while True:
        allowed_char = set("1234567890/")        
        ClaimDate = input("Enter Claim Start date (YYYY/MM/DD): ")
        if validate_date(ClaimDate, "Claim Date"):
            try:
                Claim_Date = datetime.strptime
                break
            except ValueError:
                print("Error: Please Enter Date in DD/MM/YYYY Format.") 
        elif set(ClaimDate).issubset == False:
            print("Error: Cannot Contain Special Characters or Letters")
        else:
            break

    while True:
        allowed_char = set("1234567890")  
        ClaimAmt = input("Enter Claim Amount: ")
        if ClaimAmt == "":
            print("Error: Claim Amount Cannot be Blank")
        elif not set(ClaimAmt).issubset(allowed_char):
            print("Error: Claim Amount Can Only be Numbers")
        else:
            ClaimAmt = int(ClaimAmt)
            if ClaimAmt > 1000000:
                print("Error: Claim Cannot be Greater Than 1000000")
            else:
                break
            break


    FirstCar = 869
    Discount = .25
    if CarinsNum > 1:
        InsurancePremium = 869 + (CarinsNum * 869) * 75
    else:
        InsurancePremium = 869
        
    ExtraLiabality = 0
    if ExtraLiab == "Y":
        ExtraLiabality = 130
    
    GlassPrice = 0
    if GlassCov == "Y":
        GlassPrice = 86

    LoanCar = 0
    if LoanCar == "Y":
        LoanPrice = 56

    try:
        TotalExtraCost = ExtraLiabality + LoanPrice + GlassPrice
    except NameError:
        TotalExtraCost = ExtraLiabality + GlassPrice

    TotalInsurancePremium = InsurancePremium + TotalExtraCost

    HST = TotalInsurancePremium * .15

    TotalCost = TotalInsurancePremium + HST

    if PayType != "Full":
        MonthlyPay = (TotalCost + 39.99) / 8
    elif PayType == "Down Pay":
        MonthlyPay = (TotalCost - PayAmt) / 8
        break



    # Extract year and month
    year = InvoiceDate.year
    month = InvoiceDate.month
    if month == 12:
        FirstPayDate = datetime(year + 1, 1, 1).date()
    else:
        FirstPayDate = datetime(year, month + 1, 1).date()

    print(f"First Name: {CustomerFirst}")
    print(f"Last Name: {CustomerLast}")
    print(f"Customer Address: {CustAddress}")
    print(f"City of Residence: {City}")
    print(f"Province Name: {Province}")
    print(f"Postal Code: {PostalCode}")
    print(f"Phone Number: {PhoneNum}")
    print(f"Car Incurance Number: {CarinsNum}")
    print(f"Extra Liabality Y or N: {ExtraLiabality}")
    print(f"Glass Coverage Y or N: {GlassCov}")
    print(f"Loan Car Y or N: {LoanCar}")
    print(f"Payment Type: {PayType}")
    print(f"Claim Number: {ClaimNum}")
    print(f"Claim Date: {ClaimDate}")
    print(f"Invoice Date: ", FirstPayDate.strftime('%Y-%m-%d'))
    print(f"Claim Amount: ${ClaimAmt}")
    if PayType == "Down Pay":
        print(f"Pay Amount: ${PayAmt}")
    elif PayType == "Full":
        print("Paid in Full")
    elif PayType == "Monthly":
        print(f"Monhly Pay Amount: ${MonthlyPay}")
    
    if PayType == "Down Pay":
        print(f"First Payment Due Date: {FirstPayDate}")

    with open('Const.dat', 'a') as file:
        # Append information to the file
        print(f"Additional information", file=file)

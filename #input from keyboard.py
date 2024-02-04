#named constatnts
BASERATE = 5
TAXRATE = .14
MESSAGEMIN = 100
#other variables
bill = 0
totalBill = 0
messages = 0
#user input
areaCode = input("Please enter area code ")
phoneNumber = input("please enter phone number ")
messegesSent = int(input("enter amount of messages sent for the month "))
#calculate user phonebill
if messegesSent<=MESSAGEMIN:
    bill = BASERATE
    totalBill = bill +(bill * TAXRATE)
else:
    if messegesSent>100 and messegesSent<=300:
        messages = messegesSent - MESSAGEMIN
        bill = BASERATE + (.03 * messages)
        totalBill = bill +(bill *TAXRATE)
#print statements
    print("for telephone number ("+str(areaCode) + ")" + phoneNumber)
    
    print("you sent " + str(messegesSent) + " messeges during this billing period \nyour pre-tax bill is $", format(bill,'.2f'), " your bill with tax  is $" , format(totalBill, ".2f"));


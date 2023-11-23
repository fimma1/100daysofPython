print("Welcome to the tip calculator!")

bill = float(input("What was the total bill? GHS"))

tip = int(input("How much tip would you give? GHS. eg. 10,12,15"))

people = int(input("How many people to split the bill?"))

billWithTip = tip / 100 * bill + bill
 
tipAsPercent = tip / 100
totalTipAmount = bill * tipAsPercent
totalBill = bill + totalTipAmount

print(billWithTip)
print(totalBill)

billPerPerson = totalBill / people

finalAmount = round(billPerPerson, 2)

print(f"Each person should pay GHS {finalAmount}")
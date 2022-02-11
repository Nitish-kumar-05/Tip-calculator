# DAY 2 OF 100 DAYS PYTHON CODE

# Tittle : Tip calculattor

# Description : Takes the bill amount , percentage and total people want to split.

# Inputs starts here
print("Welocome to the tip calculator!!!")
bill = float(input("How much was your total bill amount?: "))
tip = int(input("How much do you wanna tip?,choose from 10,12 or 15: "))
people = int(input("How many people want to split: "))


# Calculation starts here
percent_tip = tip / 100
total_amount = bill * percent_tip
total_bill = total_amount + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)


print(f"You have to pay {final_amount}. Thank you")

# Output : gives the final amount of tip which each person should give.
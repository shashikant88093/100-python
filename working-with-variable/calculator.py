print("Welcome to the tip calculator!")
bill=int(input("What is the total bill ?"))
tip=int(input("What percentage of tip would you linke to give ? 10 , 15 , 20"))

people = int(input("How many people you want to split the bill ?"))

tip_as_percent = tip/100

total_tip_amount = bill * tip_as_percent

total_bill = bill + total_tip_amount

bill_per_person = total_bill / people

final_amount = round(bill_per_person,2)

print(f"Each person shoud pay ${final_amount}")
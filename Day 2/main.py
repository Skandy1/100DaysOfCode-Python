print("---------------- Tip Calculator ----------------")
amount=float(input("What is the bill amount? ₹"))
percentage=int(input("How much tip would you like to give? In percentage: "))
people=int(input("How many members are present? "))
total=amount*(percentage/100)+amount
each_person=round(total/people,2)
print(f"Each person should pay ₹{each_person}")

# Write your solution here
cafe_visits = float(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
money_expenditure = float(input("How much money do you spend on the groceries in a week?"))
total_expenses = cafe_visits*lunch_price+money_expenditure
print(f"Average food expenditure: \nDaily: {total_expenses/7} euros \nWeekly: {total_expenses} euros")
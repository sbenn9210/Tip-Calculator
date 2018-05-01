
total = float(input("Please enter total:"))

tip_amount = int(input("Please enter the percentage you would like to tip:"))

total_cost = (total * (tip_amount * .01)) + total

print(f"Your total is {total_cost}")

# STEP 1: Getting Inputs
print(33*'-')
print(5*'-' + ' Financial  Visualizer ' + 5*'-')
print(33*'-')
salary = input('Annual Salary:\n')
housing = input('Monthly Housing:\n')
bills = input('Monthly Bills:\n')
food = input('Weekly Food:\n')
travel = input('Annual Travel:\n')

# STEP 2:  Validating Inputs
if salary.isnumeric() and housing.isnumeric() and bills.isnumeric() and food.isnumeric() and travel.isnumeric():
    print('All inputs confirmed valid')
else:
    print('Invalid input, please try again')

salary = float(salary)
# print('Annual Salary:\n'+ str(salary))
housing = float(housing)
# print('Monthly housing:\n'+ str(housing))
bills = float(bills)
# print('Monthly Bills:\n' + str(bills))
food = float(food)
# print('Weekly Food:\n' + str(food))
travel = float(travel)
# print('Annual Travel:\n' + str(travel))

# STEP 3: Taxes
if salary >=0 and salary <= 10000:
    tax = 0.05*salary
elif salary >= 10001 and salary <= 40000:
    tax = 0.10*salary
elif salary >= 40001 and salary <= 80000:
    tax = 0.15*salary
elif salary >= 80001:
    tax = 0.20*salary
tax=round(tax,2)

# STEP 4: Calculations

annual_housing = housing*12
annual_housing_percentage = (annual_housing/salary)*100
annual_housing_percentage_bars = int(annual_housing_percentage)
annual_housing=round(annual_housing,2)

annual_bills = bills*12
annual_bills_percentage = (annual_bills/salary)*100
annual_bills_percentage_bars = int(annual_bills_percentage)
annual_bills=round(annual_bills,2)

annual_food = food*52
annual_food_percentage = (annual_food/salary)*100
annual_food_percentage_bars = int(annual_food_percentage)
annual_food=round(annual_food,2)

annual_travel = travel
annual_travel_percentage = (annual_travel/salary)*100
annual_travel_percentage_bars = int(annual_travel_percentage)
annual_travel=round(annual_travel,2)

tax_percentage = (tax/salary)*100
tax_percentage_bars = int(tax_percentage)
tax=round(tax,2)

extra= salary - (annual_housing + annual_bills + annual_food + annual_travel + tax)
extra=round(extra,2)
extra_percentage = (extra/salary)*100
extra_percentage_bars = int(extra_percentage)

# STEP 5: Bar Chart

max_bars=int(max(annual_housing_percentage_bars, annual_bills_percentage_bars, annual_food_percentage_bars, annual_travel_percentage_bars, tax_percentage_bars, extra_percentage_bars))

print(33*'-'+max_bars*'-')

print('housing | $' + "{:>10,.2f}".format(annual_housing) + ' | ' + "{:>5.2f}".format(annual_housing_percentage) + '% | ' + '#'*annual_housing_percentage_bars)

print('  bills | $' + "{:>10,.2f}".format(annual_bills) + ' | ' + "{:>5.2f}".format(annual_bills_percentage) + '% | ' + '#'*annual_bills_percentage_bars)

print('   food | $' + "{:>10,.2f}".format(annual_food) + ' | ' + "{:>5.2f}".format(annual_food_percentage) + '% | ' + '#'*annual_food_percentage_bars)

print(' travel | $' + "{:>10,.2f}".format(annual_travel) + ' | ' + "{:>5.2f}".format(annual_food_percentage) + '% | ' + '#'*annual_food_percentage_bars)

print('    tax | $' + "{:>10,.2f}".format(tax) + ' | ' + "{:>5.2f}".format(tax_percentage) + '% | ' + '#'*tax_percentage_bars)

print('  extra | $' + "{:>10,.2f}".format(extra) + ' | ' + "{:>5.2f}".format(extra_percentage) + '% | ' + '#'*extra_percentage_bars)

print(33*'-'+max_bars*'-')


annual_salary = float(input('Enter your annual salary:'))
portion_saved = float(input('Enter the percent of your salary to save:'))
total_cost = float(input('Enter the cost of your dream home:'))
semi_annual_raise = float(input('The semi-annual salary raise:'))

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
num_months = 0

while current_savings < total_cost*portion_down_payment:
    current_savings += current_savings*r/12
    current_savings += monthly_salary*portion_saved
    
    if (num_months/6) >= 2 and num_months%6 ==0:
        monthly_salary += monthly_salary*semi_annual_raise
    num_months +=1
print('Number of months:',num_months)











annual_salary = float(input('Enter your starting annual salary:'))
total_cost = 1000000
semi_annual_raise = 0.07

portion_down_payment = 0.25
current_savings = 0
r = 0.04
monthly_salary = annual_salary/12
num_months = 0
low = 0
high = 1
portion_saved = 1.0
step = 0

while abs(current_savings - total_cost*portion_down_payment) >=100:
    current_savings =0.0
    for num_months in range(1,37):
        current_savings += current_savings*r/12
        current_savings += monthly_salary*portion_saved
        if (num_months/6) >= 1 and num_months%6 ==0:
            monthly_salary += monthly_salary*semi_annual_raise
        num_months +=1

    if portion_saved==1.0 and current_savings < total_cost*portion_down_payment:
        print('It is not possible to pay the down payment in three years.')
        break
    elif current_savings <= total_cost*portion_down_payment:
        low = portion_saved
    else:
        high = portion_saved
    portion_saved = (high + low)/2.0
    step +=1

if portion_saved != 1.0:
    print('Best saving rate: {:.2f}%'.format(portion_saved/100))
    print('Steps in bisection search:',step)


def main():
    month = int(input("How many months? "))
    income = []
    for x in range(1, month + 1, 1):
        salary = float(input("Enter income for month {}: ".format(x)))
        income.append(salary)

    calculate_cumulative(income, month)


def calculate_cumulative(income, month):
    print("\nIncome Report \n-------------")
    total = 0
    for x in range(1, month + 1):
        incomes = income[x - 1]
        total += incomes
        print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(x, incomes, total))


main()

"""cumul = income
total = [cumul[0]]
for x in range(1,len(cumul), 1):
    total.append(cumul[x] + total[x-1])

print("Income Report \n-------------")
for cal in range(0, len(income), 1):
    print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(cal+1, income[cal], total[cal]))"""
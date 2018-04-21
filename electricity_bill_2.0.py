print("Electricity bill estimator 2.0")
print()

tariff = {11: 0.244618, 31: 0.136928}
choice = int(input("Which tariff? 11 or 31: "))

while choice != tariff.keys():
    print("Incorrect. Enter again")
    choice = int(input("Which tariff? 11 or 31: "))
daily_kwh = float(input("Enter daily use in kWh: "))
billing_days = int(input("Enter number of billing days: "))

if choice == tariff:
    bill = tariff[11] * daily_kwh * billing_days
else:
    bill = tariff[31] * daily_kwh * billing_days
print()
print("Estimated bill: $", round(bill,2))
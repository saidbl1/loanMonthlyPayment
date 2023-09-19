def main():
    print(" This is a monthly payment loan calculator \n")

    loan = float(input("Entre the load amount (principal): "))
    annual_intrest = float(
        input("Enter the annual interest rate (as a percentage): "))
    years = int(input("Enter the number of years for the loan: "))

    monthly_intrest_rate = annual_intrest / 12 / 100
    amount_of_months = years * 12
    monthly_payment = loan * monthly_intrest_rate / \
        (1-(1+monthly_intrest_rate)**(-amount_of_months))

    print("The monthly payment for this loan is: %.2f" % monthly_payment)


main()
